from django.conf.urls import patterns, include, url
from blog import views

urlpatterns = patterns('',
    
    url(r'^post/(?P<post_id>\d+)/$', views.blog_post, name='blog_post'),
    url(r'^$',views.blogs, name='blogs'),
)
