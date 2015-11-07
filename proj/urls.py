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
    # API Urls
    url(r'^api/', include(router.urls)),
    url(r'^api/', include('main.api.urls')),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),
    url(r'^', include('main.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/', include('allauth.urls')),
    url(r'^blog/', include('blog.urls')),

    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps}, name="sitemap"),
    url(r'^robots\.txt', RobotTemplateView.as_view(), name="robots"),
)
