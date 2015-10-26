import requests, re, unicodedata

from django.utils import six
from django.utils.functional import allow_lazy
from django.utils.safestring import mark_safe


def slugify_no_hyphen(value):
    """
    Converts to lowercase, removes non-word characters (alphanumerics and
    underscores) and removes spaces. Also strips leading and trailing whitespace.
    Copied from django.utils.text and modified hyphen replace
    """
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub('[^\w\s-]', '', value).strip().lower()
    return mark_safe(re.sub('[-\s]+', '', value))

slugify_no_hyphen = allow_lazy(slugify_no_hyphen, six.text_type)
