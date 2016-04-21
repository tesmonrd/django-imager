"""imagersite URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

from .views import (HomeView,
                    profile_details,
                    photo_details,
                    library_view,
                    album_details,
                    CreatePhoto,
                    CreateAlbum,
                    EditAlbum,
                    EditPhoto,
                    edit_profile,
                    )
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(template_name='home.html'),
        name="home_page"),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^profile/(?P<user_id>\d+)?$', profile_details, name="profile"),
    url(r'^profile/edit', edit_profile,
        name="edit_profile"),
    url(r'^photos/(?P<user_id>\d+)/(?P<pk>[0-9]+)',
        photo_details, name="photo_details"),
    url(r'^albums/(?P<user_id>\d+)/(?P<pk>[0-9]+)',
        album_details, name="album_details"),
    url(r'^library/', library_view, name="library_view"),
    url(r'^images/photos/add', CreatePhoto.as_view(success_url="/library/")),
    url(r'^images/albums/add', CreateAlbum.as_view(success_url="/library/")),
    url(r'^images/albums/edit/(?P<user_id>\d+)/(?P<pk>[0-9]+)',
        EditAlbum.as_view(success_url="/library/"), name="edit_album"),
    url(r'^images/photos/edit(?P<user_id>\d+)/(?P<pk>[0-9]+)',
        EditPhoto.as_view(success_url="/library/"), name="edit_photo"),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
