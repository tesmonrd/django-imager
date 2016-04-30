from imager_images.models import Photo
from api.serializers import PhotoSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from api.permissions import ApiPermissions
from rest_framework import mixins, generics, viewsets


class PhotoAPI(viewsets.ModelViewSet):
    """Endpoint view for the photos."""
    quesyset = Photo.objects.filter(published='Public')
    serializer_class = PhotoSerializer
    permission_classes = (permissions.IsAuthenticated, ApiPermissions)

    def get_queryset(self):
        queryset = super(PhotoAPI, self).get_queryset()
        return queryset.filter(owner=self.request.user)
