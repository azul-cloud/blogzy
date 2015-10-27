from django.views.generic import TemplateView, ListView
# from django.views.generic import ListView

from blog.models import Post


class HomeView(TemplateView):
    template_name = "main/home.html"


class StartView(ListView):
    template_name = "main/start.html"
    model = Post


class RobotTemplateView(TemplateView):
    template_name = "main/robots.txt"
