from django.db import models
from django.conf import settings


class ActiveManager(models.Manager):
    """Use to get _is_active."""

    def get_active_profiles(self):
        """Return list of active users."""
        active_profiles = super(ActiveManager, self).get_active_profiles()
        return active_profiles.filter(user__is_active=True)


class Profile(models.Model):
    """Establish user information for the db."""

    camera = models.CharField(max_length=250)
    picture_subject = models.CharField(max_length=250)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name='profile')
    location = models.CharField(max_length=250)
    friends = models.ManyToManyField("self")
    active = ActiveManager()
    # figure out how to do friends/where to link them
