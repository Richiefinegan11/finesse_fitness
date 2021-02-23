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
            user_subscription = profile.subscription.name
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

    subscription_type = request.POST.get('subscription_type')
    request.session['subscription'] = subscription_type
    if request.user.is_authenticated:
        return redirect(reverse('subscription_checkout'))

    return redirect(reverse('account_signup'))


@login_required
def user_subscription_view(request):
    """
    Displays user's subscription view with details
    """
    profile = UserProfile.objects.get(user=request.user)

    if not profile.subscription:
        messages.error(request, "You haven't subscribed to a subscription yet.")
        return redirect(reverse('subscriptions'))

    subscription = get_object_or_404(Subscription, name=profile.subscription)
    context = {
        'subscription': subscription,
    }
    template = 'subscriptions/user_subscription.html'

    return render(request, template, context)


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
            request.session['subscription'] = subscription_type
        except KeyError:
            # If user logged in normally, redirect them
            # to the profile page
            return redirect(reverse('products'))
    
    # Retrieve data for selected subscription type
    subscription = get_object_or_404(Subscription, name=subscription_type)
    
    template = 'subscriptions/subscription_checkout.html'
    context = {
        'subscription': subscription,
        'all_subscriptions': all_subscriptions,
    }

    return render(request, template, context)


@login_required
def subscription_change(request):
    """
    Handles subscription change and adding selected subscription
    to the session
    """
    profile = UserProfile.objects.get(user=request.user)
    if not profile.subscription:
        return redirect(reverse('subscriptions'))

    if not request.POST.get('subscription_type'):
        return redirect(reverse('subscriptions'))

    all_subscriptions = Subscription.objects.all()
    subscription_type = request.POST.get('subscription_type')
    request.session['subscription'] = subscription_type
    subscription = get_object_or_404(Subscription, name=subscription_type)
    template = 'subscriptions/subscription_checkout.html'

    context = {
        'change_subscription': True,
        'subscription': subscription,
        'all_subscriptions': all_subscriptions,
    }
    return render(request, template, context)


@login_required
def subscription_update(request):
    """
    Update user's subscription in the stripe system
    and our database too
    """

    if not UserProfile.objects.get(user=request.user).subscription:
        return redirect(reverse('subscriptions'))

    stripe.api_key = settings.STRIPE_SECRET_KEY
    # user's chosen subscription
    subscription = request.session['subscription']

    # Asign correct price keys to the paid subscriptions
    if subscription == 'Gold':
        price = settings.STRIPE_PRICE_ID_GOLD
    elif subscription == 'Silver':
        price = settings.STRIPE_PRICE_ID_SILVER
    else:
        price = settings.STRIPE_PRICE_ID_BRONZE

    # Check if the user already exists in stripe system and
    # our database
    try:
        stripe_customer = StripeCustomer.objects.get(user=request.user)
        subscription = stripe.Subscription.retrieve(
            stripe_customer.stripeSubscriptionId)
        # Update existing subscription with a new one
        stripe.Subscription.modify(
            subscription.id,
            cancel_at_period_end=False,
            proration_behavior='create_prorations',
            items=[{
                'id': subscription['items']['data'][0].id,
                'price': price,
            }]
        )

        # Attach new subscription to the user's profile
        subscription_type = get_object_or_404(Subscription, name=subscription)
        profile = get_object_or_404(UserProfile, user=request.user)
        profile.subscription = subscription_type
        profile.save()

        messages.success(request, 'Congrats!! You successfully changed'
                                  ' your subscription to the '
                                  f'{subscription} subscription!')
        # Redirect the user to profiles page
        return redirect(reverse('profile'))

    # If user doesn't exist, return error
    except StripeCustomer.DoesNotExist:
        return messages.error(request, 'User does not exist')
