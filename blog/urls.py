from django.conf.urls import patterns, include, url

from . import views

app = 'blog-'

urlpatterns = patterns('',
    # post URLs
    url(r'posts/$', views.AllPostsView.as_view(), name=app + "all-posts"),
    url(r'posts/search/$', views.PostSearchView.as_view(),
        name=app + "search-posts"),
    url(r'post/create/$', views.PostCreateView.as_view(),
        name=app + "post-create"),
    url(r'post/delete/$', views.delete_post, name=app + "post-delete"),
    url(r'post/edit/(?P<pk>\d+)/$', views.PostEditView.as_view(),
        name=app + "edit-post"),

    # blog URLs
    url(r'edit/(?P<pk>\d+)/$', views.BlogEditView.as_view(),
        name=app + "edit"),
    url(r'create/$', views.BlogCreateView.as_view(), name=app + "create"),
    url(r'myblog/$', views.MyBlogView.as_view(),
        name=app + "my-blog"),
    url(r'map/$', views.BlogMapView.as_view(), name=app + "map"),
    url(r'(?P<blog>[a-zA-Z0-9-]+)/(?P<slug>[a-zA-Z0-9-]+)/$',
        views.BlogPostView.as_view(), name=app + "post"),
    url(r'(?P<slug>[a-zA-Z0-9-]+)/$', views.BlogView.as_view(),
        name=app + "blog"),
)
