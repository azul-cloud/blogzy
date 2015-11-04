from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.contrib.auth import get_user_model

from .models import PersonalBlog, Post

User = get_user_model()


class BlogHomeView(ListView):
    template_name = "blog/home.html"
    model = PersonalBlog


class BlogView(DetailView):
    template_name = "blog/blog.html"
    model = PersonalBlog


class BlogPostView(DetailView):
    template_name = "blog/post.html"
    model = Post

class BlogMapView(ListView):
    template_name = "blog/map.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super(BlogMapView, self).get_context_data(**kwargs)
        context['page'] = "map"
        return context


class AllPostsView(ListView):
    template_name = "blog/all_posts.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super(AllPostsView, self).get_context_data(**kwargs)
        context['page'] = "posts"
        return context


class AllBlogsView(ListView):
    template_name = "blog/all_blogs.html"
    model = PersonalBlog

    def get_context_data(self, **kwargs):
        context = super(AllBlogsView, self).get_context_data(**kwargs)
        context['page'] = "blogs"
        return context


class BlogSettingsView(TemplateView):
    template_name = "blog/settings.html"

    def get_context_data(self, **kwargs):
        context = super(BlogSettingsView, self).get_context_data(**kwargs)
        context['page'] = "settings"
        return context


class CreateBlogView(TemplateView):
    template_name = "blog/create.html"

    def get_context_data(self, **kwargs):
        context = super(CreateBlogView, self).get_context_data(**kwargs)
        context['page'] = "create"
        return context
