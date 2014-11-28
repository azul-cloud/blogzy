import requests
import re
import unicodedata

from django.utils import six
from django.utils.functional import allow_lazy
from django.utils.safestring import mark_safe
from django.conf import settings


def get_json_objects(url):
    # hit the api url supplied and then extract out the objects
    data = requests.get(url).json()
    objects = data.get('objects')

    return objects

def get_json(url):
    # return the raw json from a request without any extraction
    data = requests.get(url).json()

    return data

def slugify_no_hyphen(value):
    """
    Converts to lowercase, removes non-word characters (alphanumerics and
    underscores) and removes spaces. Also strips leading and
    trailing whitespace. Copied from django.utils.text and modified hyphen replace
    """
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub('[^\w\s-]', '', value).strip().lower()
    return mark_safe(re.sub('[-\s]+', '', value))
slugify_no_hyphen = allow_lazy(slugify_no_hyphen, six.text_type)


def get_place_details(place_id):
    property_search_prefix = "https://maps.googleapis.com/maps/api/place/details/"
    data_type = "json"

    # build and execute property search api call
    url = property_search_prefix + data_type + '?placeid=' + place_id + '&key=' + settings.GOOGLE_API_KEY
    data = requests.get(url).json()

    return data