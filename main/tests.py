from django.test import TestCase
from django.core.urlresolvers import reverse

class PingTests(TestCase):

    def test_fail_ping(self):
        url = '/doesnotexist/'
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)

    def test_details(self):
        url = reverse('main-home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        url = reverse('main-about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)