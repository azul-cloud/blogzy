from .base import *


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DEBUG = False
TEMPLATE_DEBUG = False

if DEBUG:
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Allow all host headers
# ALLOWED_HOSTS = ['http://tbwvtest.herokuapp.com/']

MAILGUN_ACCESS_KEY = os.environ['MAILGUN_ACCESS_KEY']
MAILGUN_SERVER_NAME = 'sandboxbea330ddebf24842829144f24a61eaa1.mailgun.org'

WEB_ROOT_URL = 'http://test.travelblogwave.com'

DATABASES = {}
DATABASES['default'] =  dj_database_url.config()

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

STATIC_URL = 'http://s3.amazonaws.com/%s' % AWS_STORAGE_BUCKET_NAME + '/'