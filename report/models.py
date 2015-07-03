from django.db import models


class PostView(models.Model):
    '''
    Store the post view
    '''
    post = models.ForeignKey('blog.Post')
    view_date = models.DateField(auto_now_add=True)
