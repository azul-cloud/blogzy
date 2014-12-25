from django.conf.urls import patterns, include, url

from main import views

app = 'main-'

urlpatterns = patterns('',
    url(r'^$', views.HomeTemplateView.as_view(), name = app + "home"),
    url(r'^about/$', views.AboutTemplateView.as_view(), 
        name = app + "about"),
    url(r'^sendcontact/$', views.send_contact, name = app + "contact"),
)
