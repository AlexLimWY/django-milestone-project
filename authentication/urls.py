from django.conf.urls import url
from authentication.views import register

urlpatterns = [
    url(r'register/$', register, name="register_link")
]