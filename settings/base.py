"""
Django settings for tbwave project.
For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
OFFLINE = False

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

env = os.environ.get('ENV')


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

    'braces',
    'django_s3_storage',
    'rest_framework',
    'crispy_forms',
    'crispy_forms_materialize',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Django-related contexts here
                "django.contrib.auth.context_processors.auth",

                # allauth context processors
                'django.template.context_processors.request',
            ],
        },
    },
]

ROOT_URLCONF = 'proj.urls'

WSGI_APPLICATION = 'proj.wsgi.application'

SITE_ID = 1

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
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']


AUTH_USER_MODEL = 'main.User'


# allauth settings
LOGIN_REDIRECT_URL = "/blog/posts/"
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_TEMPLATE_DIR = "allauth/account/"
ACCOUNT_ADAPTER = 'main.adapters.AccountAdapter'

ACCOUNT_EMAIL_VERIFICATION = None #no email verification sent. This will change.
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'

ACCOUNT_FORMS = ({
    'signup': 'main.forms.CustomSignupForm',
})

SOCIALACCOUNT_EMAIL_REQUIRED = True
SOCIALACCOUNT_TEMPLATE_DIR = "allauth/socialaccount/"

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)


# google stuff
GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']


# AWS
AWS_REGION = "us-west-2"
DEFAULT_FILE_STORAGE = 'django_s3_storage.storage.S3Storage'
AWS_S3_ACCESS_KEY_ID = os.environ['S3_KEY']
AWS_S3_SECRET_ACCESS_KEY = os.environ['S3_SECRET']
AWS_S3_BUCKET_NAME = 'dev.travelblogwave.media'


REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',)
}


CRISPY_TEMPLATE_PACK = 'materialize'
CRISPY_ALLOWED_TEMPLATE_PACKS = ('bootstrap', 'uni_form', 'bootstrap3', 'materialize')
