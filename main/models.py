import os

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse

from allauth.socialaccount.models import SocialAccount
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from blog.models import PersonalBlog, Post


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
    def get_user_image_upload_path(instance, filename):
        return os.path.join('users/' + str(instance.id) + '/' + filename)

    image = ProcessedImageField(blank=True, null=True,
                               upload_to=get_user_image_upload_path,
                               processors=[ResizeToFill(250, 250)],
                               format='JPEG',
                               options={'quality': 70})

    def __str__(self):
        return self.email

    def user_blog(self):
        # detect if the current user has started their own blog
        try:
            blog = PersonalBlog.objects.get(owner=self)
            return blog
        except PersonalBlog.DoesNotExist:
            return None
