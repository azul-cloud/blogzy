from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'forms/editpost/(?P<pk>\d+)/$', views.EditPostFormHtml.as_view()),
)
