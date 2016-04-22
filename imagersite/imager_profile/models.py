from django.db import models
from django.conf import settings


def image_path(instance, file_name):
    """Send images to media root."""
    return 'user_{0}/{1}'.format(instance.user.id, file_name)


class ActiveProfileManager(models.Manager):
    """Use to get _is_active."""

    def get_queryset(self):
        """Return list of active users."""
        qs = super(ActiveProfileManager, self).get_queryset()
        return qs.filter(user__is_active__exact=True)


class Profile(models.Model):
    """Establish user information for the db."""

    camera = models.CharField(max_length=250)
    profile_pic = models.ImageField(upload_to=image_path, null=True, blank=True)
    picture_subject = models.CharField(max_length=250)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name='profile',
                                on_delete=models.CASCADE)
    location = models.CharField(max_length=250)
    friends = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                     related_name='friend_of',
                                     symmetrical=False)
    active = ActiveProfileManager()
    objects = models.Manager()

    @property
    def is_active(self):
        """Return is_active for profile."""
        return self._is_active
