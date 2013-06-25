from django.conf.urls import patterns, url, include

from oookbook import views
from oookbook.api import v1_api

urlpatterns = patterns('',
    # All APIs exported by the application
    url(r'^api/', include(v1_api.urls)),

    # Home page of the application
    url(r'^$', views.index, name='index'),

    # Login / logout
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^accounts/logout/$', views.logout, name = 'logout'),

    # Books
    url(r'^books/?$', views.books.index, name='books.index'),
    url(r'^books/(\d+)/?', views.books.show, name='books.show'),
    url(r'^books/new', views.books.new, name='books.new'),

    url(r'^users/?$', views.users.index, name='users.index'),  
    url(r'^users/(\d+)/?', views.users.show, name='users.show'),
)