from django.contrib import admin
from profiles.models import UserProfile


@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    pass