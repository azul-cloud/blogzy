from django.test import TestCase
from django.core.urlresolvers import reverse

from django_webtest import WebTest

from testing.utils import AccessMixin
from testing.factories import NormalUserFactory, BlogUserFactory, PersonalBlogFactory, \
    PostFactory


class BlogTestSetup(TestCase):
    def setUp(self):
        self.blog_user = BlogUserFactory.create()
        self.user = NormalUserFactory.create()
        self.blog = PersonalBlogFactory.create(owner=self.blog_user)
        self.post = PostFactory.create(blog=self.blog, author=self.blog_user)
        self.prefix = "dashboard-"
        

class BlogViewTest(AccessMixin, BlogTestSetup, WebTest):
    def test_dashboard_available(self):
        # make sure the header says dashboard if user has a blog
        url = reverse("main-home")
        response = self.app.get(url, user=self.blog_user)

        assert "CREATE BLOG" not in response
        assert "DASHBOARD" in response

    def test_dashboard_blog(self):
        url = reverse("%sblog" % self.prefix, kwargs={'slug':self.blog.slug})
        response = self.app.get(url, user=self.blog_user)
        
        self.assertEqual(response.status_code, 200)

    def test_dashboard_posts(self):
        url = reverse("%sposts" % self.prefix, kwargs={'slug':self.blog.slug})
        response = self.app.get(url, user=self.blog_user)
        
        self.assertEqual(response.status_code, 200)

    def test_dashboard_stats(self):
        url = reverse("%sstats" % self.prefix, kwargs={'slug':self.blog.slug})
        response = self.app.get(url, user=self.blog_user)
        
        self.assertEqual(response.status_code, 200)

    def test_blog_post_edit(self):
        url = reverse(self.prefix + "post-edit", kwargs={'pk':self.post.id})
        self.blog_admin_access(url)

    def test_blog_post_create(self):
        url = reverse(self.prefix + "post-create")
        self.login_required(url)


class BlogFormTest(BlogTestSetup, WebTest):
    def test_edit_blog(self):
        url = reverse(self.prefix + "blog", kwargs={'blog':self.blog.slug})
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


