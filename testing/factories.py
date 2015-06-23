from factory.django import DjangoModelFactory

from django.contrib.auth import get_user_model

from blog.models import PersonalBlog, Topic, Post, UserFavorite, UserStreamBlog, \
                        BlogSubscription

User = get_user_model()


##### MAIN #####
class UserFactory(DjangoModelFactory):
    class Meta:
        model = User


class NormalUserFactory(UserFactory):
    username = 'normaluser'
    password = 'normalpassword'
    email = 'user@email.com'
    first_name = 'John'
    last_name = 'Doe'


class BlogUserFactory(UserFactory):
    username = 'bloguser'
    password = 'blogpassword'
    email = 'blog@email.com'
    first_name = 'Sir'
    last_name = 'Blogger'


class StaffFactory(UserFactory):
    username = 'staffuser'
    password = 'staffpassword'
    email = 'staff@email.com'
    first_name = 'Staff'
    last_name = 'User'
    is_staff = True


class AdminFactory(UserFactory):
    username = 'adminuser'
    password = 'adminpassword'
    email = 'admin@email.com'
    first_name = 'Admin'
    last_name = 'User'
    is_staff = True
    is_superuser = True


##### BLOG #####
class PersonalBlogFactory(DjangoModelFactory):
    # pass in owner
    class Meta:
        model = PersonalBlog

    title=u"Test Blog Title"
    description="This is my test blog"


class TopicFactory(DjangoModelFactory):
    class Meta:
        model = Topic

    title = u"Test Topic"


class PostFactory(DjangoModelFactory):
    # pass in blog and author
    class Meta:
        model = Post

    title=u"Test Post"
    body="test body text"


class UserFavoriteFactory(DjangoModelFactory):
    # pass in user and post
    class Meta:
        model = UserFavorite


class UserStreamBlogFactory(DjangoModelFactory):
    # pass in user and blog
    class Meta:
        model = UserStreamBlog


class BlogSubscriptionFactory(DjangoModelFactory):
    # pass in email and blog
    class Meta:
        model = BlogSubscription

    frequency="M"

