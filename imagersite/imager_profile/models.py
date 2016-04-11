from django.db import models
from django.conf import settings


class Profile(models.Model):
    """Establish user information for the db."""

    camera = models.CharField(max_length=250)
    picture_subject = models.CharField(max_length=250)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name='profile')
    location = models.CharField(max_length=250)
    friends = models.ManyToManyField("self")
    is_active = models.BooleanField()

    def __repr__(self):
        """Help visualize inputs."""
        name = '.'.join((__name__, self.__class__.__name__))
        return "{} is username: {}".format(name, self.user)
