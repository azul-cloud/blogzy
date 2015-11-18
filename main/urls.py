from django.conf.urls import patterns, include, url

from main import views

app = 'main-'

urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view(), name = app + "home"),
    url(r'^start$', views.StartView.as_view(), name = app + "start"),
    url(r'profile/update/$', views.ProfileUpdateView.as_view(),
        name=app + "profile-update"),
)
