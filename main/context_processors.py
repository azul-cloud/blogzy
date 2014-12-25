from django.conf import settings

from main.forms import ContactForm


def main(request):
    google_api_key = settings.GOOGLE_API_KEY
    offline = settings.OFFLINE

    return { "contact_form": ContactForm(), 'google_api_key':google_api_key,
            "offline":offline}