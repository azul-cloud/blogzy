from django.db import models
from django.contrib.auth.models import AbstractUser

from blog.models import PersonalBlog, Post

from allauth.socialaccount.models import SocialAccount


FEEDBACK_CHOICES = (
    ('N', 'New'),
    ('R', 'Replied'),
)


class TimeStampedModel(models.Model):
    '''
    An abstract base class model that provides selfupdating
    created and modified fields.
    '''
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class User(AbstractUser):
    '''
    Extended User class
    '''
    instagram = models.CharField(max_length=20, blank=True, null=True)
    twitter = models.CharField(max_length=20, blank=True, null=True)
    blog_wave = models.ManyToManyField(PersonalBlog, blank=True, null=True)

    def user_blog(self):
        # detect if the current user has started their own blog
        try:
            blog = PersonalBlog.objects.get(owner=self)
            return blog
        except:
            return None

    def google_account(self):
        # get the google account for a user if it exists
        try:
            return SocialAccount.objects.get(user=self.user)
        except:
            return None


class Contact(TimeStampedModel):
    '''
    the users can contact us through a variety of ways
    '''
    CONTACT_CHOICES = (
        ('Q', 'Question'),
        ('A', 'Anything Else'),
        ('F', 'Feedback'),
        ('P', 'Problem'),
    )

    message = models.CharField(max_length=500)
    type = models.CharField(max_length=1, choices=CONTACT_CHOICES)
    user = models.ForeignKey(User, null=True, blank=True)
    status = models.CharField(max_length=1, choices=FEEDBACK_CHOICES, default="N")

