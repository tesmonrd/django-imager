from django.db import models
from django.conf import settings

# Create your models here.

PUB_CHOICES = [('private', 'Private'), ('shared', 'Shared'), ('public', 'Public')]
PUBLIC = 'Public'


def image_path(instance, file_name):
    """Send images to media root."""
    return 'user_{0}/{1}'.format(instance.user.id, file_name)


class Photo(models.Model):
    """Class to handle photo metadata."""

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name="photos",
                             on_delete=models.CASCADE,)
    image_file = models.ImageField(upload_to=image_path, null=True)
    image_title = models.CharField(max_length=250)
    image_description = models.TextField(max_length=400)
    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(auto_now=True)

    published = models.CharField(max_length=7,
                                 choices=PUB_CHOICES,
                                 default=PUBLIC)


class Album(models.Model):
    """Class to handle album metadata."""

    album_title = models.CharField(max_length=250)
    album_description = models.TextField()
    photos = models.ManyToManyField("Photo",
                                    related_name="albums",
                                    symmetrical=False)
    alb_date_uploaded = models.DateField(auto_now_add=True)
    alb_date_modified = models.DateField(auto_now=True)
    alb_date_published = models.DateField(auto_now=True)
    published = models.CharField(max_length=7,
                                 choices=PUB_CHOICES,
                                 default=PUBLIC)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name="albums",
                             on_delete=models.CASCADE)
    cover = models.ForeignKey("Photo",
                              null=True,
                              related_name="album_cover",
                              default=None)
