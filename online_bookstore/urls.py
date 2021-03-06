"""online_bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings 
from django.conf.urls.static import static 

# from book.views import hello
from book import urls as book_urls
from authentication import urls as authentication_urls
from shopping_cart import urls as shopping_cart_urls
from checkout import urls as checkout_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^authentication/', include(authentication_urls.urlpatterns)),
    url(r'^$', include(book_urls.urlpatterns)),
    url(r'^shopping_cart/', include(shopping_cart_urls.urlpatterns)),
    url(r'^checkout/', include(checkout_urls.urlpatterns)),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)