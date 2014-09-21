from django.conf.urls import patterns, include, url

from blog import views

app = 'blog-'

urlpatterns = patterns('',
    url(r'blogs/$', views.blogs, name = app + "home"),
    url(r'blog/create/$', views.create_blog, name = app + "create"),
    url(r'(?P<blog>[\w]+)/dashboard/$', views.dashboard, name = app + "dashboard"),
    url(r'blog/post/(?P<pk>\d+)/edit/$', views.edit_post, name = app + "post-edit"),
    url(r'blog/post/create/$', views.create_post, name = app + "post-create"),

    # explore is where we search for groupings of blog posts based on region or topic
    url(r'explore/$', views.explore, name = app + "explore"),
    url(r'explore/region/(?P<region>\S+)/$', views.explore, name = app + "explore-region"),
    url(r'explore/topic/(?P<topic>\S+)/$', views.explore, name = app + "explore-topic"),
    url(r'^wave/$', views.wave, name = app + "wave"),
    url(r'^wave/(?P<action>add)/(?P<pk>\d+)/$', views.add_wave, name = app + "wave-add"),
    url(r'^wave/(?P<action>remove)/(?P<pk>\d+)/$', views.add_wave, name = app + "wave-remove"),

    url(r'^favorites/$', views.favorites, name = app + "favorites"),

    # needs to be last out of ALL urls including project URLs
    url(r'^topic/(?P<topic>[a-zA-Z0-9-]+)/$', views.topic, name = app + "topic"),
    url(r'(?P<blog>[\w]+)/(?P<post>[a-zA-Z0-9-]+)/$', views.post, name = app + "post"),
    url(r'(?P<blog>[\w]+)/$', views.blog, name = app + "blog"),
)
