from django.test import TestCase
from django.core.urlresolvers import reverse


class NavigationTests(TestCase):
    def setUp(self):
        pass

    def test_home(self):
        self.client.get(reverse('blog-home'))

    def test_blog_home(self):
        pass

    def test_blog_article(self):
        pass
