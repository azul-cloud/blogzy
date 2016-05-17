from django.conf.urls import patterns, url

from . import views
from proj.routers import router

urlpatterns = patterns('',
    url(r'forms/editpost/(?P<pk>\d+)/$', views.EditPostFormHtml.as_view()),
)
