from .base import *


DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
DATABASES['default']['NAME'] = '/home/studentrentit/dev/test.db'

#disable south migrations while testing
SOUTH_TESTS_MIGRATE = False

SUCCESS_CODES = [200, 302]