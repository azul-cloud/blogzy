from django.test import TestCase
from django.core.urlresolvers import reverse


class NavigationTests(TestCase):
    def setUp(self):
        pass

    def test_home(self):
        self.client.get(reverse('main-home'))
