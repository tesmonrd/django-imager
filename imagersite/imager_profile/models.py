from django.db import models
from django.conf import settings


class ActiveProfileManager(models.Manager):
    """Use to get _is_active."""

    def get_queryset(self):
        """Return list of active users."""
        qs = super(ActiveProfileManager, self).get_queryset()
        return qs.filter(user__is_active__exact=True)


class Profile(models.Model):
    """Establish user information for the db."""

    camera = models.CharField(max_length=250)
    picture_subject = models.CharField(max_length=250)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name='profile')
    location = models.CharField(max_length=250)
    friends = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                     related_name='friend_of')
    active = ActiveProfileManager()

    @property
    def is_active(self):
        """Return is_active for profile."""
        return self.user.is_active
