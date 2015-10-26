import os
import requests
import datetime

from django.core.urlresolvers import reverse
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from main.utils import slugify_no_hyphen


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
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
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

    def get_absolute_url(self):
        url = reverse('blog-blog', kwargs={ 'slug':self.slug })
        return url


class Post(models.Model):
    '''
    Data about blog posts. The guts of everything.
    '''

    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    blog = models.ForeignKey(PersonalBlog, related_name="posts")
    image = ProcessedImageField(upload_to=get_post_upload_path,
                                           processors=[ResizeToFill(1200, 720)],
                                           format='JPEG',
                                           options={'quality': 60})
    image_description = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    body = models.TextField()
    headline = models.CharField(max_length=100, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    active = models.NullBooleanField(default=True, blank=True, null=True)
    topics = models.ManyToManyField(Topic, null=True, blank=True)
    slug = models.SlugField(blank=True)
    lat = models.DecimalField(max_digits=12, decimal_places=6, null=True, blank=True)
    long = models.DecimalField(max_digits=12, decimal_places=6, null=True, blank=True)

    # place_id comes from Google Places API
    place_id = models.CharField(max_length=40, null=True, blank=True)
    place = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ['-create_date']
        unique_together = ("blog", "slug")

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
        url = reverse('blog-post', kwargs={'blog':self.blog.slug, 'slug':self.slug})
        return url

    def get_blog_post_id_list(self):
        '''
        return a list of ordered post ids from a blog. Used to get
        the next and previous posts
        '''
        posts = Post.objects.filter(blog=self.blog, active=True)

        post_ids = []
        for p in posts:
            post_ids.append(p.id)

        post_ids.sort()
        return post_ids

    def get_next_blog_post(self):
        # get the next post by the same blog
        curr_id = self.id
        post_ids = self.get_blog_post_id_list()

        try:
            curr_index = post_ids.index(curr_id)
            next_post_id = post_ids[curr_index + 1]
            next_post = Post.objects.get(id=next_post_id)
            return next_post
        except:
            return None


    def get_prev_blog_post(self):
        # get the previous post by the same blog
        if self.active:
            curr_id = self.id
            post_ids = self.get_blog_post_id_list()

            try:
                curr_index = post_ids.index(curr_id)
                if curr_index == 0:
                    return None
                else:
                    prev_post_id = post_ids[curr_index - 1]
                    prev_post = Post.objects.get(id=prev_post_id)
                    return prev_post
            except:
                return None

    def __str__(self):
        return self.title
