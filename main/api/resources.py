from django.contrib.auth import get_user_model

from tastypie import fields
from tastypie.resources import ModelResource, ALL
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication


class UserResource(ModelResource):
    '''
    get general information about a django user
    '''
    authentication = Authentication()
    authorization = Authorization()

    class Meta:
        user = get_user_model()
        queryset = user.objects.all()
        allowed_methods = ['get']
        excludes = ['email', 'password', 'is_superuser', 'is_staff']
        filtering = {
            'username':ALL
        }