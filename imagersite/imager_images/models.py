"""Model for user image management."""

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from django.contrib.auth.models import User

PUBLISHED_OPTIONS = (
    ('public', 'Public'),
    ('shared', 'Shared'),
    ('private', 'Private'),
)


def image_path(instance, file_name):
    """Upload file for user in media root."""
    return 'user_{0}/{1}'.format(instance.user.id, file_name)


@python_2_unicode_compatible
class Photo(models.Model):
    """Photo Model."""

    def __str__(self):
        """String Representation of user media-Photo."""
        return str(self.title)

    user = models.ForeignKey(
        User,
        related_name='photos',
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to=image_path)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now=True, null=True, blank=True)
    published = models.CharField(max_length=10, choices=PUBLISHED_OPTIONS)


@python_2_unicode_compatible
class Album(models.Model):
    """Album Model."""

    def __str__(self):
        """String Representation of user album."""
        return str(self.title)

    user = models.ForeignKey(
        User,
        related_name='albums',
        on_delete=models.CASCADE,
    )
    cover = models.ForeignKey(
        Photo,
        related_name="cover_photo",
    )
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now=True, null=True, blank=True)
    photos = models.ManyToManyField(
        Photo,
        related_name="album_photo"
    )
    published = models.CharField(
        max_length=10,
        choices=PUBLISHED_OPTIONS,
        default='public'
    )
