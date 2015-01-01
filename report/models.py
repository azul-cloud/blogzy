from django.db import models

from blog.models import Post


class PostView(models.Model):
    '''
    Store the post view
    '''
    post = models.ForeignKey(Post)
    view_date = models.DateField(auto_now_add=True)
