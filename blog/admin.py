from django.contrib import admin

from blog.models import Post, Topic, PersonalBlog, UserFavorite

admin.site.register(Post)
admin.site.register(Topic)
admin.site.register(PersonalBlog)
admin.site.register(UserFavorite)