"""Admin view for user application."""

from django.contrib import admin

from .models import Profile

admin.site.register(Profile)
