from django.conf import settings

from main.forms import FeedbackForm


def main(request):
    google_api_key = settings.GOOGLE_API_KEY

    return { "feedback_form": FeedbackForm(), 'google_api_key':google_api_key}