from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from tastypie.api import Api
from blog.api.resources import PostResource, BlogResource, UserFavoriteResource
from main.api.resources import UserResource


v1_api = Api(api_name='v1')
v1_api.register(PostResource())
v1_api.register(BlogResource())
v1_api.register(UserResource())
v1_api.register(UserFavoriteResource())

admin.autodiscover()


urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),

    url(r'^', include('main.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # 3rd party apps
    url(r'^api/', include(v1_api.urls)),
    (r'^accounts/', include('allauth.urls')),

    url(r'^internal/', include('internal.urls')),

    # blog urls need to come last because of the simple blog pattern url
    url(r'^', include('blog.urls')),
)
