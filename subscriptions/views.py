from django.db import models
from django.shortcuts import render
from django.conf import settings
from django.utils.translation import templatize

from .models import Subscription, StripeCustomer
from profiles.models import UserProfile
from django.contrib.auth.models import User

def subscriptions(request):
    """
    A view to retunr the subscriptions page
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

