from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.sitemaps import GenericSitemap

from blog.models import PersonalBlog, Post
from main.views import RobotTemplateView
from .routers import router

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
    url(r'^v1/', include(router.urls)),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),
    url(r'^', include('main.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('allauth.urls')),

    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps}, name="sitemap"),
    url(r'^robots\.txt', RobotTemplateView.as_view(), name="robots"),

    # blog urls need to come last because of the simple blog pattern url
    url(r'^blog/', include('blog.urls')),
)
