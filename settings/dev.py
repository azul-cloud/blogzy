from .base import *


DEBUG = True
TEMPLATE_DEBUG = True

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MAILGUN_ACCESS_KEY = os.environ['MAILGUN_ACCESS_KEY']
MAILGUN_SERVER_NAME = 'sandboxbea330ddebf24842829144f24a61eaa1.mailgun.org'