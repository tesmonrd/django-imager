from imager_images.models import Photo, Album
from api.serializers import PhotoSerializer, AlbumSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from api.permissions import ApiPermissions
from rest_framework import viewsets


class PhotoAPI(viewsets.ModelViewSet):
    """Endpoint view for the photos."""

    queryset = Photo.objects.filter(published='Public')
    serializer_class = PhotoSerializer
    permission_classes = (permissions.IsAuthenticated, ApiPermissions)

    def get_queryset(self):
        """Get queryset."""
        queryset = super(PhotoAPI, self).get_queryset()
        return queryset.filter(owner=self.request.user)


class AlbumAPI(viewsets.ModelViewSet):
    """Endpoint view for albums."""

    queryset = Album.objects.filter(published='Public')
    serializer_class = AlbumSerializer
    permission_classes = (permissions.IsAuthenticated, ApiPermissions)

    def get_queryset(self):
        """Get queryset."""
        queryset = super(AlbumAPI, self).get_queryset()
        return queryset.filter(owner=self.request.user)
