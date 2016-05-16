from .staging import *


# Allow all host headers

DEBUG = True
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

AWS_S3_BUCKET_NAME = 'travelblogwave.media'

MAILGUN_SERVER_NAME = 'travelblogwave.com'

WEB_ROOT_URL = 'http://www.travelblogwave.com'
