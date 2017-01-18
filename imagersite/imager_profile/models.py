"""Imager models."""

from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
import uuid

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class ActiveProfileManager(models.Manager):
    """Model manager for active profiles."""

    def get_queryset(self):
        """Return active users."""
        q = super(ActiveProfileManager, self).get_queryset()
        return q.filter(user__is_active__exact=True)


@python_2_unicode_compatible
class ImagerProfile(models.Model):
    """The Imager user and attributes."""

    objects = models.Manager()
    active = ActiveProfileManager()

    user = models.OneToOneField(
        User,
        related_name="profile",
        on_delete=models.CASCADE
    )
    imager_id = models.UUIDField(default=uuid.uuid4, editable=False)
    bio = models.TextField()
    personal_website = models.URLField(max_length=200)
    hireable = models.BooleanField(default=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    travel_radius = models.DecimalField(
        max_digits=8, decimal_places=2, null=True)
    camera_type = models.CharField(max_length=50, blank=True, null=True)
    photo_type = models.CharField(max_length=50, blank=True, null=True)
    # is_active = models.BooleanField(default=True)

    @property
    def is_active(self):
        """Return true if profile is active."""
        return self.user.is_active

    def __str__(self):
        """Display profile data as string."""
        return "User: {}, User ID: {}, About: {}, Personal Website: {}, For Hire? {}, Address: {}, Phone Number: {}, Travel Radius: {}, Camera: {}, Photography Type: {}, Active? {}".format(
            self.user, self.imager_id, self.bio, self.personal_website, self.hireable, self.address, self.phone, self.travel_radius, self.camera_type, self.photo_type, self.is_active)


@receiver(post_save, sender=User)
def make_profile_for_user(sender, instance, **kwargs):
    """."""
    new_profile = ImagerProfile(user=instance)
    new_profile.is_active = True
    new_profile.save()
