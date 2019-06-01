from django.conf.urls import url
from authentication.views import register, login, logout, index1, account_created, logged_out, invalid_login, add, add_author, add_genre, delete
from authentication.views import edit_author, delete_author, manage_authors, manage_genres, edit_genre, delete_genre, edit

urlpatterns = [
    url(r'register/$', register, name="register_link"),
    url(r'login/$', login, name='login_link'),
    url(r'logout$', logout, name="logout_link"),
    url(r'index1/$', index1, name='index1'),
    url(r'account_created/$', account_created, name='account_created'),
    url(r'logged_out/$', logged_out, name='logged_out'),
    url(r'invalid_login/$', invalid_login, name='invalid_login'),
    url(r'add/$', add, name="add"),
    url(r'add_author/$', add_author, name="add_author"),
    url(r'add_genre/$', add_genre, name="add_genre"),
    url(r'index1/delete/(?P<id>\d+)$', delete, name="delete"),
    url(r'manage_authors/$', manage_authors, name="manage_authors"),
    url(r'manage_authors/edit_author/(?P<id>\d+)$', edit_author, name="edit_author"),
    url(r'manage_authors/delete_author/(?P<id>\d+)$', delete_author, name="delete_author"),    
    url(r'manage_genres/$', manage_genres, name="manage_genres"),   
    url(r'manage_genres/edit_genre/(?P<id>\d+)$', edit_genre, name="edit_genre"),
    url(r'manage_genres/delete_genre/(?P<id>\d+)$', delete_genre, name="delete_genre"), 
    url(r'index1/edit/(?P<id>\d+)$', edit, name="edit"),    
]