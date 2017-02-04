"""Imager profile models."""

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.encoding import python_2_unicode_compatible

from phonenumber_field.modelfields import PhoneNumberField
import uuid


class ActiveProfileManager(models.Manager):
    """Model manager for active profiles."""

    def get_queryset(self):
        """Return query set of active users."""
        return super(ActiveProfileManager, self).get_queryset().filter(
            user__is_active__exact=True)


@python_2_unicode_compatible
class ImagerProfile(models.Model):
    """The Imager user and attributes."""

    objects = models.Manager()
    active = ActiveProfileManager()
    user = models.OneToOneField(
        User,
        related_name='profile',
        on_delete=models.CASCADE
    )
    CHOICE_PHOTOGRAPHY = (
        ('LANDSCAPE', 'Landscape'),
        ('PORTRAIT', 'Portrait'),
        ('BLACK_WHITE', 'Black and White'),
    )
    CHOICE_CAMERA = (
        ('CANNON', 'Cannon'),
        ('IPHONE', 'iPhone'),
        ('NIKON', 'Nikon'),
        ('POLAROID', 'polaroid'),
    )

    imager_id = models.UUIDField(default=uuid.uuid4, editable=False)
    bio = models.TextField()
    personal_website = models.URLField(max_length=200)
    hireable = models.BooleanField(default=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = PhoneNumberField(null=True)
    travel_radius = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    camera_type = models.CharField(
        max_length=50, choices=CHOICE_CAMERA, null=True)
    photo_type = models.CharField(
        max_length=100, choices=CHOICE_PHOTOGRAPHY, null=True)
    active = ActiveProfileManager()

    @property
    def is_active(self):
        """Return true if profile is active."""
        return self.user.is_active

    def __str__(self):
        """Display profile data as string."""
        return ("User: {}, User ID: {}, About: {}, Personal Website: {}, " +
                "For Hire? {}, Address: {}, Phone Number: {}, " +
                "Travel Radius: {}, Camera: {}, Photography Type: {}, " +
                "Active? {}".format(
                    self.user, self.imager_id, self.bio, self.personal_website,
                    self.hireable, self.address, self.phone,
                    self.travel_radius, self.camera_type, self.photo_type,
                    self.is_active))


@receiver(post_save, sender=User)
def make_profile_for_user(sender, instance, **kwargs):
    """User registers and receives a profile."""
    if kwargs['created']:
        new_profile = ImagerProfile(user=instance)
        # new_profile.camera = 'N'
        new_profile.save()
