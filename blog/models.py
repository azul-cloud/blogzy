import os
import requests
import datetime

from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from main.utils import slugify_no_hyphen, get_place_details


def get_post_upload_path(instance, filename):
    blog_id = instance.blog.id
    return os.path.join('blog/' + str(blog_id) + '/' + filename)

def get_blog_upload_path(instance, filename):
    blog_id = instance.id
    return os.path.join('blog/' + str(blog_id) + '/main_' + filename)


class PersonalBlog(models.Model):
    """
    Data about a personal blog for a specific user. The user can upload
    metadata about their blog to give it a personalized feel
    """
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=50)
    image = ProcessedImageField(blank=True, null=True, upload_to=get_blog_upload_path,
                               processors=[ResizeToFill(1200, 720)],
                               format='JPEG',
                               options={'quality': 60})
    description = models.TextField(help_text="Tell us a bit about your blog and yourself")
    slug = models.SlugField(unique=True, blank=True, editable=False)
    twitter = models.CharField(max_length=15, blank=True, null=True,
        help_text="What is your Twitter handle? (Don't put @)")
    facebook = models.CharField(max_length=40, blank=True, null=True,
        help_text="Just the last part of your facebook URL (i.e. travelblogwave)")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # add identifying slug field on save
        self.slug = slugify_no_hyphen(self.title)
        super(PersonalBlog, self).save(*args, **kwargs)

    def get_absolute_url(self):
        url = reverse('blog-blog', kwargs={ 'slug':self.slug })
        return url

    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return static("img/blog_default.png")

    def get_last_post_with_loc(self):
        for post in self.posts.all():
            if post.lat and post.lng:
                return post


class PostManager(models.Manager):

    def public(self):
        return self.filter(public=True)

    def map_eligible(self):
        return self.public().filter(
            lat__isnull=False,
            lng__isnull=False,
        )


class Post(models.Model):
    """
    Data about blog posts. The guts of everything.
    """
    blog = models.ForeignKey(PersonalBlog, related_name="posts")
    image = ProcessedImageField(upload_to=get_post_upload_path,
                                           processors=[ResizeToFill(1200, 720)],
                                           format='JPEG',
                                           options={'quality': 60},
                                           help_text='main image for your article')
    image_description = models.CharField(max_length=100, help_text="What is your image? (ex: San Andres Beach Colombia)")
    title = models.CharField(max_length=50)
    body = models.TextField()
    headline = models.CharField(max_length=100, null=True, blank=True,
        help_text="100 characters to catch reader's attention")
    create_date = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=False, help_text="Should the article be publically viewable now?")
    slug = models.SlugField(blank=True, editable=False)
    lat = models.DecimalField(max_digits=12, decimal_places=6, null=True, blank=True)
    lng = models.DecimalField(max_digits=12, decimal_places=6, null=True, blank=True)

    # place_id comes from Google Places API
    place_id = models.CharField(max_length=40, null=True, blank=True)
    place = models.CharField(max_length=100, null=True, blank=True)

    objects = PostManager()

    class Meta:
        ordering = ['-create_date']
        unique_together = ("blog", "slug")

    def set_location(self):
        # use the google places API to set the latitude and longitude
        details = get_place_details(self.place_id)
        location = details.get("result").get("geometry").get("location")

        self.lat = location.get("lat")
        self.lng = location.get("lng")


    def save(self, *args, **kwargs):
        # add identifying slug field on save
        self.slug = slugify(self.title)

        # set the lat and long
        if self.place_id:
            self.set_location()

        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        url = reverse('blog-post', kwargs={
            'blog':self.blog.slug,
            'slug':self.slug
        })
        return url

    def get_blog_post_id_list(self):
        """
        return a list of ordered post ids from a blog. Used to get
        the next and previous posts
        """
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
