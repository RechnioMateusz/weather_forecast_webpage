"""Views for user application."""

from django.shortcuts import render

from .models import Profile


def main_view(request):
    """Main view for user application. Displays info about users.

    ===========================================================================
    |                      ONLY FOR DEBBUGING PURPOSES                        |
    ===========================================================================
    """

    return render(
        request=request,
        template_name="user/main.html",
        context={
            "profiles": Profile.objects.all()
        }
    )
