from django.test import TestCase
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.models import User


class InternalTestSetup(TestCase):
    def setUp(self):
        self.prefix = "internal-"

        self.admin = User.objects.create_user('admin_tester', 
            'admin@somewhere.com', 'testpassword')
        self.admin.is_staff = True
        self.admin.save()

    def login_admin(self):
        self.client.login(username=self.admin.username, 
            password='testpassword')

class InternalModelTest(InternalTestSetup):
    pass


class InternalViewTest(InternalTestSetup):
    def test_home(self):
        url = reverse(self.prefix + "home")
        
        anon_response = self.client.get(url)
        self.assertEqual(anon_response.status_code, 302)

        self.login_admin()
        admin_response = self.client.get(url)
        self.assertContains(admin_response, "Internal Home")

    def test_feedback(self):
        url = reverse(self.prefix + "feedback")
        
        anon_response = self.client.get(url)
        self.assertEqual(anon_response.status_code, 302)
        
        self.login_admin()
        admin_response = self.client.get(url)
        self.assertContains(admin_response, "Feedback")




class InternalFormTest(InternalTestSetup):
    pass