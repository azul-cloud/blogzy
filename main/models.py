from django.db import models
from django.contrib.auth.models import AbstractUser

from blog.models import PersonalBlog, Post

from allauth.socialaccount.models import SocialAccount


FEEDBACK_CHOICES = (
    ('N', 'New'),
    ('R', 'Replied'),
)


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides selfupdating
    created and modified fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    """
    Extended User class
    """
    instagram = models.CharField(max_length=20, blank=True, null=True)
    twitter = models.CharField(max_length=20, blank=True, null=True)
    blog_wave = models.ManyToManyField(PersonalBlog, blank=True, null=True)

    def user_blog(self):
        # detect if the current user has started their own blog
        try:
            blog = PersonalBlog.objects.get(owner=self)
            return blog
        except PersonalBlog.DoesNotExist:
            return None
