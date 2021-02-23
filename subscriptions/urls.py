from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscriptions, name='subscriptions'),
    path('subscription_type/', views.subscription_type, name='subscription_type'),
    path('subscription_checkout/', views.subscription_checkout,
         name='subscription_checkout'),
    path('subscription_change/', views.subscription_change,
         name="subscription_change"),
]
