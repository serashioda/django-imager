"""Model for user image management."""

from __future__ import unicode_literals

from django.db import models
# from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


PUBLISHED_OPTIONS = (
    ('public', 'public'),
    ('shared', 'shared'),
    ('private', 'private'),
)


def image_path(instance, file_name):
    """Upload file for user in media root."""
    return 'user_{0}/{1}'.format(instance.user.id, file_name)


@python_2_unicode_compatible
class Photo(models.Model):
    """Photo Model."""


@python_2_unicode_compatible
class Album(models.Model):
    """Album Model."""


def __str__(self):
    """String Representation of User media."""
