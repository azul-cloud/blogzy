"""
Django settings for tbwave project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

env = os.environ.get('ENV')

if env == 'test':
    # in heroku test env
    DEBUG = True
    TEMPLATE_DEBUG = True
    ALLOWED_HOSTS = ['test.travelblogwave.com']
    SECRET_KEY = '3iy-!-d$!pc_ll$8$elg&cpr@*tfn-d5&#9ag=)%#()t$$5%5^'

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )

    MAILGUN_ACCESS_KEY = 'key-47816e24fe42b25aa3ade1ef01f9275d'
    MAILGUN_SERVER_NAME = 'sandboxbea330ddebf24842829144f24a61eaa1.mailgun.org'

elif env == 'prod':
    # in heroku prod env
    DEBUG = False
    TEMPLATE_DEBUG = False
    ALLOWED_HOSTS = ['www.travelblogwave.com']
    SECRET_KEY = '3iy-!-d$!pc_ll$#$elg#cpr@*tfn-d5&nAag=)%#()t$$5%5^'

    if DEBUG:
        STATICFILES_DIRS = (
            os.path.join(BASE_DIR, 'static'),
        )
    else:
        STATIC_ROOT = os.path.join(BASE_DIR, 'static')

    MAILGUN_ACCESS_KEY = 'key-47816e24fe42b25aa3ade1ef01f9275d'
    MAILGUN_SERVER_NAME = 'travelblogwave.com'

else:
    # local, or lost
    DEBUG = True
    TEMPLATE_DEBUG = True
    ALLOWED_HOSTS = []
    SECRET_KEY = '3iy-!-d$!pc_1l$#$elg#cpr@*tfn-d5&JAag=)%#()t$$5%5^'

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )

    MAILGUN_ACCESS_KEY = 'key-47816e24fe42b25aa3ade1ef01f9275d'
    MAILGUN_SERVER_NAME = 'sandboxbea330ddebf24842829144f24a61eaa1.mailgun.org'


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',

    'main',
    'blog',
    'internal',

    'tastypie',
    'south',
    'allauth',
    'crispy_forms',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'storages',
    'pagination',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'pagination.middleware.PaginationMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "main.context_processors.main",
    "django.contrib.auth.context_processors.auth",

    # Required by allauth template tags
    "django.core.context_processors.request",

    # allauth specific context processors
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

ROOT_URLCONF = 'proj.urls'

WSGI_APPLICATION = 'proj.wsgi.application'

SITE_ID = 1

DATABASES = {}
DATABASES['default'] =  dj_database_url.config()

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# run the project without internet
OFFLINE = True


import sys
if 'test' in sys.argv or 'test_coverage' in sys.argv: #Covers regular testing and django-coverage
    DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
    DATABASES['default']['NAME'] = '/home/studentrentit/dev/test.db'

#disable south migrations while testing
SOUTH_TESTS_MIGRATE = False

SUCCESS_CODES = [200, 302]

# Crispy settings
CRISPY_TEMPLATE_PACK = 'bootstrap3'


# allauth settings
LOGIN_REDIRECT_URL = "/"
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_TEMPLATE_DIR = "allauth/account/"
SOCIALACCOUNT_TEMPLATE_DIR = "allauth/socialaccount/"
ACCOUNT_EMAIL_REQUIRED = True
SOCIALACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = None #no email verification sent. This will change.

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

# google stuff
GOOGLE_API_KEY = 'AIzaSyCsPHVZewbLPsJgz3oB8v8JzaFzNpyR0NA'

# aws s3
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_S3_SECURE_URLS = False       # use http instead of https
AWS_QUERYSTRING_AUTH = False     # don't add complex authentication-related query parameters for requests
AWS_S3_ACCESS_KEY_ID = 'AKIAJJFP34XQF2OPJD5A'     # enter your access key id
AWS_S3_SECRET_ACCESS_KEY = 'vQGWfysb5a1ZmPyq4BD3VSyyTC9AFVCJcHLVyOuh' # enter your secret access key
AWS_STORAGE_BUCKET_NAME = 'travelblogwave.media'

PAGINATION_TEMPLATE_PACK = "bootstrap3"

EMAIL_BACKEND = 'django_mailgun.MailgunBackend'