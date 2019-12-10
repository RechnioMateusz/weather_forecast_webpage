"""Views for forecast application."""

from django.views.generic import TemplateView


class MainView(TemplateView):
    """Main view for forecast application. Displays info about current weather.

    **Attributes**
        :template_name: Name of template. [str]
    """

    template_name = "forecast/main.html"
