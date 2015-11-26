from django.conf import settings
from django.core.urlresolvers import reverse

from allauth.account.adapter import DefaultAccountAdapter


class AccountAdapter(DefaultAccountAdapter):

  def get_login_redirect_url(self, request):
    threshold = 5

    if (request.user.last_login - request.user.date_joined).seconds < threshold:
        return reverse('blog-create')
    else:
        return settings.LOGIN_REDIRECT_URL
