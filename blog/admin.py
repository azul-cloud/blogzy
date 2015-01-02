from django.contrib import admin

from .models import Post, Topic, PersonalBlog, UserFavorite, BlogSubscription

admin.site.register(Post)
admin.site.register(BlogSubscription)
admin.site.register(Topic)
admin.site.register(PersonalBlog)
admin.site.register(UserFavorite)