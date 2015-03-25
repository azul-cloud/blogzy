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

class BlogViewTest(AccessMixin, BlogTestSetup, WebTest):
    def test_create_blog(self):
        url = reverse(self.prefix + "create")
        response = self.app.get(url)

        assert response.status_code == 200

    def test_dashboard_available(self):
        # make sure the header says dashboard if user has a blog
        url = reverse("main-home")
        response = self.app.get(url, user=self.blog_user)

        assert "CREATE BLOG" not in response
        assert "DASHBOARD" in response

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

    def test_blog_dashboard(self):
        url = reverse(self.prefix + "dashboard", kwargs={'blog':self.blog.slug})
        blog_user_response = self.app.get(url, user=self.blog_user)

        assert self.blog.title in blog_user_response

    def test_create_blog(self):
        url = reverse(self.prefix + "create")
        self.login_required(url)

    def test_blog_post_edit(self):
        url = reverse(self.prefix + "post-edit", kwargs={'pk':self.post.id})
        self.blog_admin_access(url)

    def test_blog_post_create(self):
        url = reverse(self.prefix + "post-create")
        self.login_required(url)

    def test_explore(self):
        url = reverse(self.prefix + "explore")
        response = self.app.get(url)

        assert "Filter to fit your interest" in response

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
        
        response = form.submit()

        # 302 because it redirects to the dashboard
        self.assertEqual(response.status_code, 302)

    def test_edit_blog(self):
        url = reverse(self.prefix + "dashboard", kwargs={'blog':self.blog.slug})
        form = self.app.get(url, user=self.blog_user).forms['blog-edit-form']
        form['description'].value = 'This is the edited description for the test blog.'
        response = form.submit()

        # make sure the description was changed successfully
        self.assertContains(response, form["description"].value)
        self.assertNotContains(response, self.blog.description)

    def test_create_post(self):
        url = reverse(self.prefix + "post-create")

        form = self.app.get(url, user=self.blog_user).forms['blog-post-create-form']
        form["place_id"] = "ak34dfkjo2la"
        form["title"] = "My New Test Post"
        form["active"] = True
        form["body"] = 'This is my new post.'
        form["headline"] = "This is my test post, read it."
        form["image"] = ""
        form["image_description"] = "this is the alt tag"
 
        response = form.submit()
        assert form["body"].value in response
        

    def test_edit_post(self):
        url = reverse(self.prefix + "post-edit", kwargs={'pk':self.post.id})

        form = self.app.get(url, user=self.blog_user).forms['blog-post-edit-form']
        form["body"] = 'This is my updated body. Sexy huh?'

        response = form.submit()
        assert form["body"].value in response
        assert self.post.body not in response

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


