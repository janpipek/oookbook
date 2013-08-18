from django.conf.urls import patterns, url, include

from oookbook import views
from oookbook.api import v1_api

urlpatterns = patterns('',
    # All APIs exported by the application
    url(r'^api/', include(v1_api.urls)),

    # Home page of the application
    url(r'^$', views.index, name='index'),

    # Login / logout
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^logout/$', views.logout, name = 'logout'),
    url(r'^welcome/$', views.welcome, name = 'welcome'),

    # Books
    url(r'^books/$', views.books.index, name='books.index'),
    url(r'^books/(\d+)/$', views.books.show, name='books.show'),
    # url(r'^books/(?P<book_id>\d+)/borrow/$', views.loans.borrow, name='books.borrow'),
    url(r'^books/new/$', views.books.new, name='books.new'),

    # Loans
    url(r'^loans/$', views.loans.index, name='loans.index'),
    url(r'^loans/new/$', views.loans.new, name='loans.new'),

    # Users
    url(r'^users/$', views.users.index, name='users.index'),  
    url(r'^users/(\d+)/$', views.users.show, name='users.show'),
)