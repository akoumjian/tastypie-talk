# myapp/api.py
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from demo.models import Foo


class FooResource(ModelResource):
    class Meta:
        queryset = Foo.objects.all()
        resource_name = 'foo'
        authorization = Authorization()
