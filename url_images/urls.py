from django.conf.urls.defaults import patterns
from url_images import DjangoImageHandler

resizer = DjangoImageHandler()

urlpatterns = patterns('',
    (r'^.*$', resizer),
)
