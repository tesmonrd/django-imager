from django.conf.urls import url, include
from api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'photos', views.PhotoAPI)

urlpatterns = [
    url(r'^v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework'))
]
