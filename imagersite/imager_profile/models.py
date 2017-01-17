"""Imager models."""

from django.db import models
from django.contrib.auth.models import User
import uuid

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class ImagerProfile(models.Model):
    """The Imager user and attributes."""

    user = models.OneToOneField(
        User,
        related_name="profile",
        on_delete=models.CASCADE
    )
    camera_type = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField()
    personal_website = models.URLField(max_length=200)
    hireable = models.BooleanField(default=True)
    travel_radius = models.DecimalField(
        max_digits=8, decimal_places=2, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    photo_type = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    imager_id = models.UUIDField(default=uuid.uuid4, editable=False)


@receiver(post_save, sender=User)
def make_profile_for_user(sender, instance, **kwargs):
    """."""
    new_profile = ImagerProfile(user=instance)
    new_profile.is_active = True
    new_profile.save()
