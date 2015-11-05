from django.views.generic import TemplateView, ListView
# from django.views.generic import ListView

from blog.models import Post


class HomeView(TemplateView):
    template_name = "main/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['post_list'] = Post.objects.map_eligible()
        return context


class StartView(ListView):
    template_name = "main/start.html"
    model = Post


class RobotTemplateView(TemplateView):
    template_name = "main/robots.txt"
