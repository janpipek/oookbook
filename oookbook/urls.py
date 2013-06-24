from django.conf.urls import patterns, url, include

from oookbook import views
from oookbook.api import v1_api

urlpatterns = patterns('',
    url(r'^api/', include(v1_api.urls)),
    url(r'^$', views.index, name='index')
)