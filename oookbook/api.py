from tastypie.resources import ModelResource
from tastypie.api import Api
from oookbook.models import Book

class BookResource(ModelResource):
    class Meta:
        queryset = Book.objects.all()
        resource_name = 'book'

v1_api = Api(api_name='v1')
v1_api.register(BookResource())