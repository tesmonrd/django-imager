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

from .views import HomeView, profile_details, photo_details, library_view
from django.conf import settings
# from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# login_required automatically send individual to login page (wrap around the url)
# only for templates, if function view, place it in function


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(template_name='home.html'),
        name="home_page"),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^profile/(?P<user_id>\d+)?$', profile_details, name="profile"),
    url(r'^photos/(?P<user_id>[0-9]+)/(?P<photo_id>[0-9]+)',
        photo_details,
        name="photo_details"),
    url(r'^library/', library_view, name="library_view"),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
