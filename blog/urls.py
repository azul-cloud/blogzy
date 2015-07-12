from django.conf.urls import patterns, include, url

from blog import views

app = 'blog-'

urlpatterns = patterns('',

    url(r'blog/create/$', views.create_blog, name=app + "create"),
    url(r'recent/$', views.RecentPostListView.as_view(), name=app + "recent-posts"),

    # explore is where we search for groupings of blog posts based on region or topic
    url(r'explore/map/(?P<place_id>\S+)/$', views.ExploreMapListView.as_view(),
        name=app + "explore-map"),
    url(r'explore/map/$', views.ExploreMapListView.as_view(),
        name=app + "explore-map-base"),

    url(r'place/(?P<place_id>\S+)/$', views.place, name=app + "place"),
    url(r'^wave/$', views.wave, name=app + "wave"),
    url(r'^wave/(?P<action>add)/(?P<pk>\d+)/$', views.add_wave, name=app + "wave-add"),
    url(r'^wave/(?P<action>remove)/(?P<pk>\d+)/$', views.add_wave, name=app + "wave-remove"),

    url(r'^favorites/$', views.favorites, name=app + "favorites"),

    # needs to be last out of ALL urls including project URLs
    url(r'^topic/(?P<topic>[a-zA-Z0-9-]+)/$', views.topic, name=app + "topic"),
    url(r'(?P<blog>\S+)/(?P<post>[a-zA-Z0-9-]+)/$', views.post, name=app + "post"),
    url(r'(?P<slug>\S+)/$', views.BlogDetailView.as_view(), name=app + "blog"),

    # url(r'blog/post/(?P<pk>\d+)/edit/$', views.edit_post, name=app + "post-edit"),
    # url(r'blog/post/create/$', views.create_post, name=app + "post-create"),
)
