from django.db import models
from django.conf import settings

# Create your models here.

PUB_CHOICES = [('Private', 'Private'), ('Shared', 'Shared'), ('Public', 'Public')]
PUBLIC = 'Public'


class Photo(models.Model):
    """Class to handle photo metadata."""

    image = models.ImageField()
    photographer = models.ForeignKey(settings.AUTH_USER_MODEL,
                                     related_name="photos",
                                     default=None)
    ablums = models.ManyToManyField('Album', related_name="photos")
    image_title = models.CharField(max_length=250)
    image_description = models.TextField()
    date_uploaded = models.DateField(auto_now=True)
    date_modified = models.DateField(auto_now_add=True)
    date_published = models.DateField(auto_now_add=True)

    published = models.CharField(max_length=7,
                                 choices=PUB_CHOICES,
                                 default=PUBLIC)


class Album(models.Model):
    """Class to handle album metadata."""

    album_title = models.CharField(max_length=250)
    album_description = models.TextField()
    alb_date_uploaded = models.DateField(auto_now=True)
    alb_date_modified = models.DateField(auto_now_add=True)
    alb_date_published = models.DateField(auto_now_add=True)
    published = models.CharField(max_length=7,
                                 choices=PUB_CHOICES,
                                 default=PUBLIC)
    photographer = models.ForeignKey(settings.AUTH_USER_MODEL,
                                     related_name="albums",
                                     default=None)
    # still need cover and user specificity
