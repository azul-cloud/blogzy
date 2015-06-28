import factory

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth import get_user_model

from django_webtest import WebTest

from .models import BlogSubscription
from report.models import PostView
from testing.utils import AccessMixin
from testing.factories import NormalUserFactory, BlogUserFactory, PersonalBlogFactory, \
    TopicFactory, PostFactory, UserFavoriteFactory, UserStreamBlogFactory, BlogSubscriptionFactory

User = get_user_model()


class BlogTestSetup(TestCase):
    def setUp(self):
        self.blog_user = BlogUserFactory.create()
        self.user = NormalUserFactory.create()
        self.blog = PersonalBlogFactory.create(owner=self.blog_user)
        self.topic = TopicFactory.create()
        self.post = PostFactory.create(blog=self.blog, author=self.blog_user)
        self.user_favorite = UserFavoriteFactory.create(user=self.user, post=self.post)
        self.user_stream_blog = UserStreamBlogFactory.create(
            user=self.user,
            blog=self.blog
        )
        self.blog_subscription = BlogSubscriptionFactory.create(
            email=self.user.email,
            blog=self.blog
        )
        
        self.prefix = "blog-"


class BlogModelTest(BlogTestSetup):
    def test_blog_subscription_count(self):
        count = self.blog.subscription_count()

        assert count == 1

    def test_blog_subscription_latest(self):
        # get when the latest weekly and monhtly email were sent
        latest_dict = self.blog.last_subscription_sent()
        

class BlogViewTest(AccessMixin, BlogTestSetup, WebTest):
    def test_create_blog(self):
        url = reverse(self.prefix + "create")
        response = self.app.get(url)

        assert response.status_code == 200

    def test_blog_home(self):
        url = reverse(self.prefix+"blog", kwargs={'slug':self.blog.slug})
        response = self.app.get(url)

        assert self.blog.title in response

    def test_blog_post(self):
        url = self.post.get_absolute_url()
        response = self.app.get(url)
        assert self.post.title in response

        # make sure the meta content is correct
        assert '<meta name="title" content="%s | %s">' % (self.post.blog.title, self.post.title) in response
        assert '<meta name="description" content="%s" />' % self.post.headline

    def test_blog_topic(self):
        url = reverse(self.prefix+"topic", kwargs={'topic':self.topic.slug})
        response = self.app.get(url)

        assert self.topic.title in response

    def test_create_blog(self):
        url = reverse(self.prefix + "create")
        self.login_required(url)

    def test_explore(self):
        url = reverse(self.prefix + "recent-posts")
        response = self.app.get(url)

        assert "The Most Recent Posts" in response

    def test_explore_map(self):
        url = reverse(self.prefix + "explore-map", kwargs={
            'place_id':'ChIJQ77mcJFvR44RegoSeGbgTFU'
        })
        response = self.app.get(url)

        assert response.status_code == 200

    def test_topic(self):
        url = reverse(self.prefix + "topic", kwargs={'topic':self.topic.slug})
        response = self.app.get(url)

        assert self.topic.title in response

    def test_wave(self):
        url = reverse(self.prefix + "wave")

    def test_wave_add(self):
        url = reverse(self.prefix + "wave-add", kwargs={"pk":self.blog.id,
            "action":"add"})
        response = self.app.get(url, user=self.user)

        assert response.status_code == 200

    def test_wave_remove(self):
        url = reverse(self.prefix + "wave-remove", kwargs={"pk":self.blog.id,
            "action":"remove"})
        response = self.app.get(url, user=self.user)
        
        assert response.status_code == 200

    def test_favorites(self):
        url = reverse(self.prefix + "favorites")
        self.login_required(url)


class BlogFormTest(BlogTestSetup, WebTest):
    def test_create_blog(self):
        url = reverse(self.prefix + "create")

        form = self.app.get(url, user=self.blog_user).forms['blog-create-form']
        form["title"] = "Joes Blog"
        form["description"] = "This is Joe's Blog. It's a test."
        
        response = form.submit().follow()

        self.assertEqual(response.status_code, 200)

    def test_add_subscription(self):
        url = reverse(self.prefix+"post", kwargs={
            'blog':self.blog.slug,
            'post':self.post.slug
        })

        form = self.app.get(url, user=self.blog_user).forms['blog-subscription-form']
        post = {
            "email":self.blog_user.email,
            "frequency":"M",
        }
        response = form.submit()

        assert response.status_code == 200


