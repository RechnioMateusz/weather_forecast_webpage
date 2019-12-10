"""URLs for user application."""

from django.urls import path

from .views import main_view

urlpatterns = [
    path("", main_view, name="user-main"),
]
