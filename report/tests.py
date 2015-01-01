from django.test import TestCase
from django.core.urlresolvers import reverse

from blog.tests import BlogTestSetup

'''
The report app gives the project a way to keep reports organized, easily 
maintainable and expandable. There are different sections for different 
user groups that will be able to see different reports, or shared reports
with different data sets based on permissions.
'''

# class ReportTestSetup(TestCase):
#     def setUp(self):
#         BlogTestSetup.setUp(self)


# class ReportViewTests(ReportTestSetup):
#     def test_admin_home(self):
#         self.login_admin(self)
#         response = self.client.get(reverse('report-admin-home'))
#         self.assertEqual(response.status_code, 200)



