from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import ListView, TemplateView

from braces.views import StaffuserRequiredMixin


class HomeTemplateView(StaffuserRequiredMixin, TemplateView):
    '''
    home page for the internal pages. This will probably be some sort
    of a dashboard eventually
    '''
    template_name = "internalcontent/home.html"