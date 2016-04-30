from rest_framework import serializers
from imager_images.models import Photo, Album


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    """Serialize photo."""

    class Meta:
        """Info."""

        model = Photo
        fields = ['user', 'image_file', 'image_title', 'image_description', 
                  'date_uploaded', 'date_modified', 'date_published', 'published']


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    """Serialize album."""

    class Meta:
        """Info."""

        model = Album
        fields = ['user', 'album_title', 'album_description', 'alb_date_uploaded',
                  'alb_date_published', 'published']
