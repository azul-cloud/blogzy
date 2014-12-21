from .staging import *


# Allow all host headers
ALLOWED_HOSTS = ['http://www.travelblogwave.com/', 
    'http://tbwv.herokuapp.com/']

MAILGUN_SERVER_NAME = 'travelblogwave.com'

DEBUG = False
TEMPLATE_DEBUG = False

 # AWS_STORAGE_BUCKET_NAME = 'travelblogwave.media'