"""Views for device application."""

from django.shortcuts import render

from .models import Device


def main_view(request):
    """Main view for device application. Displays info about devices.

    ===========================================================================
    |                      ONLY FOR DEBBUGING PURPOSES                        |
    ===========================================================================
    """

    return render(
        request=request,
        template_name="user/main.html",
        context={
            "profiles": Device.objects.all()
        }
    )
