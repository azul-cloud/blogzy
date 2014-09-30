import json
import requests

from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from main.utils import get_json_objects, get_json
from main.models import Feedback
from blog.models import Topic


def home(request):
    topics = Topic.objects.all()

    return render(request, "maincontent/home.html", {'topics':topics})


def about(request):

    return render(request, "maincontent/about.html", {})


def send_feedback(request):
    # have users send feedback to us. If user is logged in, attach user.
    if request.method == "POST" and request.is_ajax:
        feedback = request.POST.get('feedback')

        if request.user.is_authenticated():
            user = request.user
        else:
            user = None

        feedback_obj = Feedback(feedback=feedback, user=user)
        feedback_obj.save()

        return HttpResponse("feedback sent successfully")

    return HttpResponse("not an AJAX Post request")


# def mail(request):
#
#     send_mail('Subject here', 'Here is the message.', 'travelblogwave@gmail.com',
#         ['awwester@gmail.com'], fail_silently=False)
#
#     return HttpResponse("sent!")

def robots(request):
    return render(request, 'maincontent/robots.txt', {})