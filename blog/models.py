import os
import requests

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django.conf import settings

from main.utils import slugify_no_hyphen, get_place_details


def get_blog_upload_path(instance, filename):
    blog_id = instance.id
    return os.path.join('blog/' + str(blog_id) + '/' + filename)


def get_post_upload_path(instance, filename):
    blog_id = instance.blog.id
    return os.path.join('blog/' + str(blog_id) + '/' + filename)


class Topic(models.Model):
    '''
    grouping of all the topics that a blog post can be grouped under. Allows
    users to search for a specific type of blog post
    '''
    title = models.CharField(max_length=20)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        url = reverse('blog-topic', kwargs={'topic':self.slug})
        return url

    def save(self, *args, **kwargs):
        self.slug = slugify_no_hyphen(self.title)
        super(Topic, self).save(*args, **kwargs)


class PersonalBlog(models.Model):
    '''
    Data about a personal blog for a specific user. The user can upload
    metadata about their blog to give it a personalized feel
    '''
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    description = models.TextField()
    logo = models.ImageField(upload_to=get_blog_upload_path, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    disqus = models.CharField(max_length=30, blank=True, null=True)
    twitter = models.CharField(max_length=15, blank=True, null=True)
    twitter_widget_id = models.CharField(max_length=18, blank=True, null=True)
    facebook = models.CharField(max_length=40, blank=True, null=True)
    instagram = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # add identifying slug field on save
        self.slug = slugify_no_hyphen(self.title)
        super(PersonalBlog, self).save(*args, **kwargs)

    def total_subscription_count(self):
        # TODO: get the total number of subscriptions for a blog
        count = 0
        return count

    def get_absolute_url(self):
        url = reverse('blog-blog', kwargs={ 'blog':self.slug })
        return url

    def google_id(self):
        # returns the google id associated with the google account of the blog owner
        try:
            google_account = self.owner.profile.google_account()
            id = google_account.uid
            return id
        except:
            return None


class Post(models.Model):
    '''
    Data about blog posts. The guts of everything.
    '''
    author = models.ForeignKey(User)
    blog = models.ForeignKey(PersonalBlog)
    image = models.ImageField(upload_to=get_post_upload_path, null=True, blank=True)
    title = models.CharField(max_length=50)
    body = models.TextField()
    headline = models.CharField(max_length=100, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    topics = models.ManyToManyField(Topic, null=True, blank=True)
    views = models.IntegerField(default=0, blank=True, editable=False)
    slug = models.SlugField(unique=True, blank=True)
    lat = models.DecimalField(max_digits=12, decimal_places=6, null=True, blank=True)
    long =  models.DecimalField(max_digits=12, decimal_places=6, null=True, blank=True)


    # place_id comes from Google Places API
    place_id = models.CharField(max_length=40, null=True, blank=True)
    place = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        ordering = ['-create_date']

    def set_location(self):
        # use the google places API to set the latitude and longitude
        details = get_place_details(self.place_id)
        location = details.get("result").get("geometry").get("location")

        self.lat = location.get("lat")
        self.long = location.get("lng")


    def save(self, *args, **kwargs):
        # add identifying slug field on save
        self.slug = slugify(self.title)

        # set the lat and long
        if self.place_id and not self.lat and not self.long:
            self.set_location()

        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        url = reverse('blog-post', kwargs={'blog':self.blog.slug, 'post':self.slug})
        return url

    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return settings.STATIC_URL + 'img/logo_dark.png'

    def get_topics(self):
        # return the topics that have been listed for the post object
        topics = self.topics.all()

        if topics:
            return topics
        else:
            return None

    def __str__(self):
        return self.title


class UserFavorite(models.Model):
    '''
    Mark a favorite post for a user so that it is easily accessible
    in the future
    '''
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    create_date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "post")

    def __str__(self):
        return self.user.username + ' for ' + self.post.title


class UserStreamBlog(models.Model):
    '''
    Add a blog to stream to get notifications on certain events, such
    as when they put out a new post. Users will be able to see the blog
    posts in their stream
    '''
    user = models.ForeignKey(User)
    blog = models.ForeignKey(PersonalBlog)
    new_post_email = models.BooleanField(default=False)
    email_newsletter = models.BooleanField(default=False)
    create_date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "blog")

    def __str__(self):
        return self.user.username + ' for ' + self.blog.title


