from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from adimas import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'adimas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    #url(r'^tinymce/', include('tinymce.urls')),
)
urlpatterns += patterns('', (
        r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': 'static'}
))