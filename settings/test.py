from .base import *


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    },
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
MAILGUN_ACCESS_KEY = os.environ['MAILGUN_ACCESS_KEY']
MAILGUN_SERVER_NAME = 'sandboxbea330ddebf24842829144f24a61eaa1.mailgun.org'