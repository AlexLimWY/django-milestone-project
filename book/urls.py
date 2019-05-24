from django.conf.urls import url
from .views import index

urlpatterns = [
    url(r'^$', index, name='index'),
    # url(r'add/$', add_post),
    # url(r'edit/(?P<id>\d+)$', edit_post),
]