from django.conf.urls import patterns, include, url

from main import views

app = 'main-'

urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view(), name = app + "home"),
)
