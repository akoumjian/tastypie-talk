from django.conf.urls.defaults import patterns, include
from tastypie.api import Api
from demo.api import FooResource

api = Api(api_name='v1')
api.register(FooResource())

urlpatterns = patterns('',
    (r'^api/', include(api.urls)),
)
