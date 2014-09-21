from django.conf.urls import patterns, include, url

from internal import views


app = 'internal-'


urlpatterns = patterns('',
    url(r'^$', views.home, name = app + "home"),
    url(r'^feedback/$', views.feedback, name = app + "feedback"),
)