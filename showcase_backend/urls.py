from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from router import get_api_urls


urlpatterns = patterns(
    '',
    url(
        r'^admin/',
        include(admin.site.urls)
    ),
    url(
        r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
    url(
        r'^api/',
        include(get_api_urls())
    ),
    url(
        r'^api/',
        include('showcase_backend.users.urls')
    ),
)

if settings.ENVIRONMENT == 'DEVELOPMENT':
    urlpatterns = urlpatterns +\
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
