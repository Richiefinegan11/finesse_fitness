from django.contrib import admin
from subscriptions.models import Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'free_delivery',
        
    )
