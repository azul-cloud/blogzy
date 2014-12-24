from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model

class MainTestSetup(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'main_test_user', 
            'testuser@domain.com',
            'testpassword'
        )

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