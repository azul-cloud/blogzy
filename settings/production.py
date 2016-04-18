from .staging import *


# Allow all host headers

DEBUG = False
TEMPLATE_DEBUG = False

if DEBUG:
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

AWS_S3_BUCKET_NAME = 'travelblogwave.media'

MAILGUN_SERVER_NAME = 'travelblogwave.com'

WEB_ROOT_URL = 'http://www.travelblogwave.com'
