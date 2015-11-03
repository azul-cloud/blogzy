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


class AllPostsView(ListView):
    template_name = "blog/all_posts.html"
    model = Post


class AllBlogsView(ListView):
    template_name = "blog/all_blogs.html"
    model = PersonalBlog


class BlogSettingsView(TemplateView):
    template_name = "blog/settings.html"


class CreateBlogView(TemplateView):
    template_name = "blog/create.html"
