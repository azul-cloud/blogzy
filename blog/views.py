from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.contrib.auth import get_user_model

from .models import PersonalBlog, Post

User = get_user_model()


class PageMixin(object):
    page = ""

    def get_context_data(self, **kwargs):
        context = super(PageMixin, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context


class BlogHomeView(ListView):
    template_name = "blog/home.html"
    model = PersonalBlog


class BlogView(DetailView):
    template_name = "blog/blog.html"
    model = PersonalBlog


class BlogPostView(DetailView):
    template_name = "blog/post.html"
    model = Post


class BlogMapView(PageMixin, ListView):
    template_name = "blog/map.html"
    model = Post
    page = "map"


class AllPostsView(PageMixin, ListView):
    template_name = "blog/all_posts.html"
    model = Post
    page = "posts"


class AllBlogsView(PageMixin, ListView):
    template_name = "blog/all_blogs.html"
    model = PersonalBlog
    page = "blogs"


class BlogSettingsView(PageMixin, TemplateView):
    template_name = "blog/settings.html"
    page = "settings"


class CreateBlogView(PageMixin, TemplateView):
    template_name = "blog/create.html"
    page = "create"
