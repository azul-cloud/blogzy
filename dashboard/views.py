from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView


from braces.views import LoginRequiredMixin, UserPassesTestMixin

from blog.models import PersonalBlog, Post
from .forms import BlogPostCreateForm, BlogPostUpdateForm, BlogEditForm


class DashboardBaseView(LoginRequiredMixin, UserPassesTestMixin):
    """
    a view that all dashboard views should inherit from
    """
    def get_login_url(self):
        user = self.request.user
        if user.is_authenticated() and user.user_blog():
            return reverse('dashboard-blog', kwargs={
                'slug': user.user_blog().slug
            })
        else:
            return reverse('main-home')

    def test_func(self, user):
        """
        check if the user is the owner of the blog
        """
        kwargs = self.kwargs
        if 'slug' in kwargs:
            slug = kwargs['slug']
        elif 'blog' in kwargs:
            slug = kwargs['blog']

        try:
            if slug:
                PersonalBlog.objects.get(slug=slug, owner=self.request.user)
                return True
        except PersonalBlog.DoesNotExist:
            pass

        return False


class Blog(DashboardBaseView, UpdateView):
    template_name = "dashboardcontent/blog.html"
    model = PersonalBlog
    form_class = BlogEditForm

    def get_context_data(self, **kwargs):
        context = super(Blog, self).get_context_data(**kwargs)
        context['page'] = 'blog'
        return context


class PostMixin(object):
    """
    include logic involved in all the post views
    """
    model = Post
    posts_page = ""

    def get_context_data(self, **kwargs):
        context = super(PostMixin, self).get_context_data(**kwargs)
        # determines which side nav is active
        context['page'] = 'posts'

        # determines which post nav is active
        context['posts_page'] = self.posts_page
        return context


class Posts(DashboardBaseView, PostMixin, DetailView):
    template_name = "dashboardcontent/posts.html"
    posts_page = "overview"
    model = PersonalBlog

    def get_context_data(self, **kwargs):
        context = super(Posts, self).get_context_data(**kwargs)
        context['object_list'] = Post.objects.filter(blog=self.get_object())
        return context


class PostCreate(DashboardBaseView, PostMixin, CreateView):
    template_name = "dashboardcontent/post_create.html"
    posts_page = "create"
    form_class = BlogPostCreateForm
    model = PersonalBlog

    def form_valid(self, form):
        """
        save the blog to the object
        """
        form.instance.blog = self.get_object()
        form.instance.author = self.request.user
        return super(PostCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PostCreate, self).get_context_data(**kwargs)
        context['personalblog'] = self.get_object()
        return context


class PostEdit(DashboardBaseView, PostMixin, UpdateView):
    template_name = "dashboardcontent/post_edit.html"
    posts_page = "edit"
    form_class = BlogPostUpdateForm
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostEdit, self).get_context_data(**kwargs)
        context['personalblog'] = self.get_object().blog
        return context


class Stats(DashboardBaseView, DetailView):
    model = PersonalBlog
    template_name = "dashboardcontent/stats.html"

    def get_context_data(self, **kwargs):
        context = super(Stats, self).get_context_data(**kwargs)
        context['page'] = 'stats'
        return context
