from django.conf.urls import patterns, url

from . import views

app = 'dashboard-'

urlpatterns = patterns('',
    url(r'(?P<blog>\S+)/posts/(?P<pk>\d+)/$', views.PostEdit.as_view(),
        name=app + "post-edit"),
    url(r'(?P<slug>\S+)/posts/create/$', views.PostCreate.as_view(),
        name=app + "post-create"),
    url(r'(?P<slug>\S+)/posts/$', views.Posts.as_view(),
        name=app + "posts"),

    url(r'(?P<slug>\S+)/stats/$', views.Stats.as_view(),
        name=app + "stats"),

    url(r'(?P<slug>\S+)/$', views.Blog.as_view(),
        name=app + "blog"),
)
