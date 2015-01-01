from django.conf.urls import patterns, url

from report import views

prefix = 'report-'

urlpatterns = patterns('',
    url(r'^admin/$', views.admin_home, name=prefix + 'admin-home'),
)