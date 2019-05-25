from django.conf.urls import url
from authentication.views import register, login, logout, index1, account_created, logged_out, invalid_login

urlpatterns = [
    url(r'register/$', register, name="register_link"),
    url(r'login/$', login, name='login_link'),
    url(r'logout$', logout, name="logout_link"),
    url(r'index1/$', index1, name='index1'),
    url(r'account_created/$', account_created, name='account_created'),
    url(r'logged_out/$', logged_out, name='logged_out'),
    url(r'invalid_login/$', invalid_login, name='invalid_login'),
]