from django.contrib import admin

from .models import Feedback, User


admin.site.register(Feedback)
admin.site.register(User)