#8.889 seconds before refactor

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model

from testing.factories import UserFactory


class MainTestSetup(TestCase):
    def setUp(self):
        self.user = UserFactory.create()


class MainViewTest(MainTestSetup):
    def test_home(self):
        url = reverse('main-home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "CREATE BLOG")

    def test_about(self): 
        url = reverse('main-about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_robots(self):
        url = reverse('robots')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_sitemap(self):
        url = reverse('sitemap')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

