import stripe

from django.conf import settings
from django.db import models
from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse, HttpResponse


from .models import Subscription, StripeCustomer
from profiles.models import UserProfile
from django.contrib import messages
from django.contrib.auth.models import User


def subscriptions(request):
    """
    A view to return the subscriptions page
    """

    # Get the subscription entries

    subscriptions = Subscription.objects.all()
    template = 'subscriptions/subscriptions.html'
    if request.user.is_anonymous:
        context = {
            'subscriptions': subscriptions,
        }
    else:
        profile = UserProfile.objects.get(user=request.user)
        if profile.subscription:
            user_subscription = profile.subscription.subscription_level
            context = {
                'user_subscription': user_subscription,
                'subscriptions': subscriptions,
            }
        else:
            context = {
                'subscriptions': subscriptions,
            }
    return render(request, template, context)


def subscription_type(request):
    """
    Catch the subscription type selected by the user, 
    store it in the session and redirect the user to signup
    """

    subscription_type = request.POST.get('subcription_type')
    request.session['subscription'] = subscription_type
    if request.user.is_authenticated:
        return redirect(reverse('subscription_checkout'))

    return redirect(reverse('account_signup'))


@login_required
def subscription_checkout(request):
    """
    Get user's selected subscription, display it and allow the user
    to change the subscription
    """

    # Get all subscriptions
    all_subscriptions = Subscription.objects.all()

    # Check if the user has a subscription, if not re-direct to
    # subscription change
    profile = UserProfile.objects.get(user=request.user)
    if profile.subscription:
        return redirect(reverse('subscription_change'))
    # If user is updating selected subscription, the
    # subscription_type to the new value
    if request.GET.get('subscription-new'):
        subscription_type = request.GET.get('subscription-new')
        # add subscription type to session to retrieve for stripe
        request.session['subscription'] = subscription_type
    # If user logged in after registering, get subscription_type
    # from session
    else:
        try:
            # get user selected subscription
            subscription_type = request.session['subscription']
        except KeyError:
            # If user logged in normally, redirect them
            # to the profile page
            return redirect(reverse('profile'))
    
    # Retrieve data for selected subscription type
    subscription = get_object_or_404(Subscription, subscription_level=subscription_type)

    template = 'subscriptions/subscription_checkout.html'
    context = {
        'subscription': subscription,
        'all_subscriptions': all_subscriptions,
    }

    return render(request, template, context)

