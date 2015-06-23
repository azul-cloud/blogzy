import json
import requests

from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.views.generic import TemplateView

from .utils import get_json_objects, get_json
from blog.models import Topic, Post


class HomeTemplateView(TemplateView):
    # show the home page
    template_name = "maincontent/home.html"

    def get_context_data(self, **kwargs):
        topics = Topic.objects.all()
        recent_posts = Post.objects.filter(active=True)[:3]
        return {'topics':topics, 'recent_posts':recent_posts}


class AboutTemplateView(TemplateView):
    template_name = "maincontent/about.html"


class RobotTemplateView(TemplateView):
    template_name = "maincontent/robots.txt"


