from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import PersonalBlog, Post


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
