from django.db import models

# Create your models here.

PUB_CHOICES = [('Private', 'Private'), ('Shared', 'Shared'), ('Public', 'Public')]
PUBLIC = 'Public'


class Photo(models.Model):
    """Class to handle photo metadata."""

    image = models.ImageField()
    # insert info about photo/url/path?
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
    # still need cover and user specificity
    published = models.CharField(max_length=7,
                                 choices=PUB_CHOICES,
                                 default=PUBLIC)
