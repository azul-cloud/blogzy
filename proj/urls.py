from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.sitemaps import GenericSitemap

from tastypie.api import Api
from blog.models import PersonalBlog, Post
from blog.api.resources import PostResource, BlogResource, UserFavoriteResource
from main.api.resources import UserResource
from main.views import RobotTemplateView


v1_api = Api(api_name='v1')
v1_api.register(PostResource())
v1_api.register(BlogResource())
v1_api.register(UserResource())
v1_api.register(UserFavoriteResource())

admin.autodiscover()

#get dictionaries and build the sitemap
post_dict = {
    'queryset': Post.objects.all(),
    'changefreq': 'monthly',
}
blog_dict = {
    'queryset': PersonalBlog.objects.all(),
    'changefreq': 'daily'
}
sitemaps = {
    "post": GenericSitemap(post_dict, priority=1.0),
    "blog": GenericSitemap(blog_dict, priority=0.8)
}

urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),
    url(r'^', include('main.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    (r'^accounts/', include('allauth.urls')),
    url(r'^internal/', include('internal.urls')),
    url(r'^reports/', include('report.urls')),
    
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps}, name="sitemap"),
    url(r'^robots\.txt', RobotTemplateView.as_view(), name="robots"),

    # blog urls need to come last because of the simple blog pattern url
    url(r'^', include('blog.urls')),
)
