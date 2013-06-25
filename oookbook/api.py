from tastypie.resources import ModelResource
from tastypie.api import Api
from oookbook.models import Book
from django.contrib.auth.models import User

class BookResource(ModelResource):
    class Meta:
        queryset = Book.objects.all()
        resource_name = 'book'

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields = [ 'first_name', 'last_name', 'username' ]

v1_api = Api(api_name='v1')
v1_api.register(BookResource())
v1_api.register(UserResource())