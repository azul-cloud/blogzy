from .staging import *


# Allow all host headers

DEBUG = False
TEMPLATE_DEBUG = False

if DEBUG:
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )
else:
    """ STATICFILES_DIRS can come from settings.staging if debug is True
        so we need to override it here
    """
    STATICFILES_DIRS = ""
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

AWS_STORAGE_BUCKET_NAME = 'travelblogwave.media'

MAILGUN_SERVER_NAME = 'travelblogwave.com'

WEB_ROOT_URL = 'http://www.travelblogwave.com'