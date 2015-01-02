from django.core.mail import send_mail
from django.test import TestCase
from django.test.utils import override_settings

'''
django overrides the EMAIL_BACKED, so we need to override the override in order
to test Mailgun
'''
@override_settings(EMAIL_BACKEND='django_mailgun.backends.MailgunBackend')


class MailgunTestSetup(TestCase):
    def setUp(self):
        pass


class MailgunFunctionTest(MailgunTestSetup):
    def test_send_mail(self):
        send =send_mail('subject', 'body', 'travelblogwave@gmail.com', ['awwester@gmail.com'])
        self.assertEqual(send, 1)