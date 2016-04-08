from django.db import models
from django.conf import settings
# Create your models here.


class Profile(models.Model):
    """Establish user information for the db."""

    camera = models.CharField(max_length=250)
    picture_subject = models.CharField(max_length=250)
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    location = models.CharField(max_length=250)
    friends = models.ManyToManyField("self")
    is_active = models.BooleanField()
