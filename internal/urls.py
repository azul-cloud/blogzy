from django.conf.urls import patterns, include, url

from internal import views


app = 'internal-'

urlpatterns = patterns('',
    url(r'^$', views.HomeTemplateView.as_view(), name = app + "home"),
    url(r'^feedback/$', views.FeedbackListView.as_view(), 
        name = app + "feedback"),
)