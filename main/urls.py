from django.conf.urls import patterns, include, url

from main import views

app = 'main-'

urlpatterns = patterns('',
    url(r'^$', views.home, name = app + "home"),
    url(r'^about/$', views.about, name = app + "about"),
    url(r'^sendfeedback/$', views.send_feedback, name = app + "send-feedback"),
)
