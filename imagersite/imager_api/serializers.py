from rest_framework import serializers
from imager_images.models import Photo


class PhotoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Photo
        fields = ['user', 'image_file', 'image_title', 'image_description', 
                  'date_uploaded', 'date_modified', 'date_published', 'published']
