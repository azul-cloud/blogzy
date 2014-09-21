from django.db import models
from django.contrib.auth.models import User

from blog.models import PersonalBlog, Post

from allauth.socialaccount.models import SocialAccount


FEEDBACK_CHOICES = (
    ('N', 'New'),
    ('R', 'Replied'),
)


class UserProfile(models.Model):
    '''
    extended information about a user
    '''
    user = models.OneToOneField(User, related_name="profile")
    instagram = models.CharField(max_length=20, blank=True, null=True)
    twitter = models.CharField(max_length=20, blank=True, null=True)
    blog_wave = models.ManyToManyField(PersonalBlog, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def user_blog(self):
        # detect if the current user has started their own blog
        try:
            blog = PersonalBlog.objects.get(owner=self.user)
            return blog
        except:
            return None

    def google_account(self):
        # get the google account for a user if it exists
        try:
            return SocialAccount.objects.get(user=self.user)
        except:
            return None


class Feedback(models.Model):
    # have a user submit feedback to us
    feedback = models.CharField(max_length=500)
    user = models.ForeignKey(User, null=True, blank=True)
    status = models.CharField(max_length=1, choices=FEEDBACK_CHOICES, default="N")
    create_date = models.DateField(auto_now_add=True)


# create a user profile if it doesn't exist
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])