import requests, json, datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.db import IntegrityError
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import ProcessFormView

from .models import PersonalBlog, Post, Topic, UserFavorite
from .forms import BlogCreateForm, BlogEditForm, BlogPostCreateForm, BlogPostEditForm,\
                   CreateBlogSubscriptionForm
from .utils import get_favorites, get_wave_blog_list, get_map_posts
from main.utils import get_json_objects, get_json, get_place_details
from report.models import PostView


class PlaceDetailsMixin(object):
    '''
    get place details and return the data in context
    '''
    def get_details(self):
        # get the coordinates to center based on the place_id kwarg
        place_id = self.kwargs["place_id"]
        place_details = get_place_details(place_id)
        return place_details

    def get_context_data(self, **kwargs):
        context = super(PlaceDetailsMixin, self).get_context_data(**kwargs)
        place_details = self.get_details()
        context["place_details"] = place_details
        context["loc"] = place_details.get("result").get("geometry").get("location")
        return context


class BlogDetailView(DetailView):
    '''
    Show the blog home page which will have a list of the latest articles
    as well as a map of all their posts
    '''
    template_name = "blogcontent/blog.html"
    model = PersonalBlog

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        # get a user's wave list
        if self.request.user.is_authenticated():
            context['wave_bool_list'] = get_wave_blog_list(self.request.user)

        #get the posts and map posts for the blog object
        context['posts'] = Post.objects.filter(blog=self.get_object(), 
            active=True)
        context['post_list'] = get_map_posts(context['posts'])
        context['loc'] = self.object.last_post_loc()

        return context


class ExploreMapListView(PlaceDetailsMixin, ListView):
    template_name = "blogcontent/explore_map.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super(ExploreMapListView, self).get_context_data(**kwargs)
        context["map_zoom"] = 11
        return context


class RecentPostListView(ListView):
    '''
    Search for blog posts. Can search by different places/topics.
    '''
    template_name = "blogcontent/recent.html"
    queryset = Post.objects.filter(active=True)


def post(request, **kwargs):
    '''
    show an individual blog post
    '''
    blog_slug = kwargs['blog']
    blog = get_object_or_404(PersonalBlog, slug=blog_slug)

    post_slug = kwargs['post']
    post = get_object_or_404(Post, slug=post_slug, blog=blog)
    id = post.id

    status = ""
    alert_message = ""
    
    # record the view if not the blog owner
    if request.user != post.blog.owner:
        if request.user != "admin":
            post.record_view()

    form = CreateBlogSubscriptionForm()

    # get other posts to display in the template
    other_posts = Post.objects.filter(blog=post.blog, active=True)\
        .exclude(id=id)[:3]

    # detect if post is in the user's favorites
    favorites = get_favorites(request.user)

    if request.method == "POST":
        # save the blog subscription on post
        form = CreateBlogSubscriptionForm(request.POST)
        if form.is_valid():
            try:
                subscription = form.save(commit=False)
                subscription.blog = blog
                form.save()
                alert_message="You have been added to the newsletter for %s" % blog
                status = "success"
            except IntegrityError:
                status = "error"
                alert_message = "It appears that you are already signed up for this %s's newsletters" % blog
                pass

    return render(request, "blogcontent/post.html", 
        {'post':post, 'other_posts':other_posts, 'favorites':favorites,
         'form':form, 'status':status, 'alert_message':alert_message})


def blog_subscribe(request):
    '''
    receive an ajax post request to subscribe to a blog
    '''
    if request.method == "POST":
        status = ""
        alert_message = ""
        form = CreateBlogSubscriptionForm()

        if request.method == "POST":
            # save the blog subscription on post
            form = CreateBlogSubscriptionForm(request.POST)
            if form.is_valid():
                try:
                    subscription = form.save(commit=False)
                    subscription.blog = blog
                    form.save()
                    alert_message="You have been added to the newsletter for %s" % blog
                    status = "success"
                except IntegrityError:
                    status = "error"
                    alert_message = "It appears that you are already signed up for this %s's newsletters" % blog
                    pass


def topic(request, **kwargs):
    # return the posts that are listed under a certain topic
    topic_slug = kwargs["topic"]
    topic = Topic.objects.get(slug=topic_slug)
    posts = Post.objects.filter(topics__in=[topic.id], active=True)

    return render(request, "blogcontent/topic.html", {'posts':posts, 'topic':topic})


def wave(request):
    '''
    show the articles that a user has added to their stream
    '''
    user = request.user

    if user.is_authenticated():
        # get the blogs that are in a user's wave
        wave_blog_list = get_wave_blog_list(request.user)

        blogs = request.user.blog_wave.all()

        post_set = []
        for b in blogs:
            for p in b.post_set.filter(active=True):
                post_set.append(p)

        return render(request, "blogcontent/wave.html",
                      {'blogs':blogs, 'posts':post_set, 'wave_blog_list':wave_blog_list})
    else:
        # user not logged in
        wave_blog_list = None
        return render(request, "blogcontent/wave_register.html", {})


def place(request, **kwargs):

    place_id = kwargs['place_id']
    place = get_place_details(place_id).get('result')

    posts = Post.objects.filter(place_id=place_id)

    return render(request, "blogcontent/place.html",
        {'place': place, 'posts':posts})


@login_required
def add_wave(request, **kwargs):
    '''
    add a blog to a user's blog wave
    '''
    if request.method == "POST":
        if request.is_ajax():
            id = kwargs["pk"]
            action = kwargs["action"]

            blog = get_object_or_404(PersonalBlog, id=id)

            if action == "add":
                # add the blog to the current user's blog wave
                request.user.blog_wave.add(blog)
                return HttpResponse("added blog " + blog.title)
            elif action == "remove":
                # remove the blog from the current user's blog wave
                request.user.blog_wave.remove(blog)
                return HttpResponse("removed blog " + blog.title)
        else:
            return HttpResponse("Not an ajax post")
    else:
        return HttpResponse("Not a Post request")


@login_required
def create_blog(request):
    '''
    have a user create a new blog
    '''
    status = ""
    alert_message = ""
    form = BlogCreateForm()

    if request.method == "POST":
        # attempt save the blog object through the API
        form = BlogCreateForm(request.POST, request.FILES)

        if form.is_valid():
            title = request.POST["title"]
            description = request.POST["description"]

            try:
                blog = PersonalBlog(
                    owner=request.user,
                    title=title,
                    description=description
                )
                blog_obj = blog.save()
                blog.save()

                # saved and redirect to create a post
                # status = "new"
                # form = BlogEditForm(request.POST, request.FILES)

                redirect_url = reverse('dashboard-blog', kwargs={'blog':blog.slug})

                return redirect(redirect_url)

            except IntegrityError:
                status = "error"
                alert_message = "That blog name is already taken, please choose another."
                pass
        else:
            alert_message = "Your blog data was not valid! Please fix the errors."
            status = "error"

    return render(request, "blogcontent/blog_create.html", {'form':form, 'status':status,
                                                    'alert_message':alert_message})




@login_required
def favorites(request):
    '''
    display a list of posts that a user has marked as favorite
    '''
    favorites = get_favorites(request.user)['objects']

    # favorites_url = settings.BASE_URL + "/api/v1/userfavorite/?user__username=" + user.username
    # favorites = get_json(favorites_url)

    return render(request, "blogcontent/favorites.html", {'favorites':favorites})

