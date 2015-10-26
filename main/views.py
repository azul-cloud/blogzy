from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "main/home.html"


class RobotTemplateView(TemplateView):
    template_name = "main/robots.txt"
