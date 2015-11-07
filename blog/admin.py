from django.contrib import admin

from .models import Post, PersonalBlog

admin.site.register(Post)
admin.site.register(PersonalBlog)
