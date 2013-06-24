from django.conf.urls import patterns, include, url

from oookbook import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
    # Examples:
    # url(r'^$', 'oookbooksite.views.home', name='home'),
    # url(r'^oookbooksite/', include('oookbooksite.foo.urls')),
)