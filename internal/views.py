from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

from main.models import Feedback


@staff_member_required
def home(request):
    # the home page for the internal portal. Will display various internal tasks.

    return render(request, "internalcontent/home.html", {})


@staff_member_required
def feedback(request):
    # manage feedback that was submitted by users

    feedback = Feedback.objects.all()

    return render(request, "internalcontent/feedback.html", {'feedback':feedback})
