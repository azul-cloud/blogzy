from django.contrib.auth import get_user_model
from django.db.models import Q
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView

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

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        context['last_post_with_loc'] = self.object.get_last_post_with_loc()
        return context


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


class PostSearchView(AllPostsView):

    def post(self, request, *args, **kwargs):

        self.queryset = Post.objects.filter(
            Q(title__icontains=self.request.POST["search"]) |
            Q(headline__icontains=self.request.POST["search"]) |
            Q(body__icontains=self.request.POST["search"]))
        return self.get(request)

    # def get_queryset(self):
    #     print(self.kwargs["search_term"])
    #     return Post.objects.filter(
    #         title__icontains=self.kwargs["search_term"])


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
