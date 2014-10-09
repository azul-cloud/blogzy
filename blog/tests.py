from django.test import TestCase
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.models import User

from blog.models import Topic, PersonalBlog


# class DataTests(TestCase):
#
#     def setUp(self):
#         self.user = User.objects.create_user('datatester', 'tester@somewhere.com', 'testpassword')
#
#     def test_fail_create_blog(self):
#
#
#     def test_create_blog(self):
#         blog = PersonalBlog.objects.create(title=u"test blog title", owner_id=self.user.id)
#
#     def test_create_post(self):
#         return False


class PingTests(TestCase):

    url_prefix = 'blog-'

    def test_fail_ping(self):
        # make sure we're running ok
        url = '/doesnotexist/'
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)

    def test_create_blog_get(self):
        # GET portion of the create blog
        url = reverse(self.url_prefix + 'create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_explore(self):
        url = reverse(self.url_prefix + 'explore')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # TODO: Create region
    # def test_explore_region(self):
    #     url = reverse(url_prefix + 'explore-region', kwargs={})
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)

    # TODO: Create topic
    # def test_explore_country(self):
    #     url = reverse(url_prefix + 'explore-topic')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)

    # TODO: Create User
    # def test_dashboard(self):
    #     url = reverse(url_prefix + 'dashboard')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)

    # TODO: Create User
    # def test_post_create(self):
    #     url = reverse(url_prefix + 'create-post')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)

    # TODO: Create User, Create Post
    # def test_post_edit(self):
    #     url = reverse(url_prefix + 'edit-post')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)

    # TODO: Create User
    # def test_wave(self):
    #     url = reverse(url_prefix + 'wave')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)

    # TODO: Create User, Create Favorite
    # def test_post_edit(self):
    #     url = reverse(url_prefix + 'favorites')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)

    # TODO: Create User, Create Blog
    # def test_blog(self):
    #     url = reverse(url_prefix + 'blog')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)

    # TODO: Create User, Create Blog, Create Post
    # def test_blog(self):
    #     url = reverse(url_prefix + 'blog')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)