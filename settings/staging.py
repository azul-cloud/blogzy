from .base import *

import dj_database_url


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DEBUG = os.environ.get("DEBUG", False)
TEMPLATE_DEBUG = DEBUG

# Allow all host headers
ALLOWED_HOSTS = ['http://tbwvtest.herokuapp.com/']

MAILGUN_ACCESS_KEY = os.environ['MAILGUN_ACCESS_KEY']
MAILGUN_SERVER_NAME = 'sandboxbea330ddebf24842829144f24a61eaa1.mailgun.org'

WEB_ROOT_URL = 'http://test.travelblogwave.com'

DATABASES = {}
DATABASES['default'] =  dj_database_url.config()
