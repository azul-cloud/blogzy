from django.conf.urls import patterns, include, url

from . import views

app = 'blog-'

urlpatterns = patterns('',

    url(r'(?P<blog>[a-zA-Z0-9-]+)/(?P<slug>[a-zA-Z0-9-]+)/$', views.BlogPostView.as_view(),
    name=app + "post"),
    url(r'(?P<slug>[a-zA-Z0-9-]+)/$', views.BlogView.as_view(), name=app + "blog"),
    url(r'$', views.BlogHomeView.as_view(), name=app + "home"),
)
