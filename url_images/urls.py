from django.conf.urls.defaults import *
from url_images import DjangoImageHandler

resizer = DjangoImageHandler()

urlpatterns = patterns('',
    (r'^.*$', resizer),
)
