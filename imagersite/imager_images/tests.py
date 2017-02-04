"""Tests for imager_images app."""

from django.test import TestCase

from imager_images.models import Photo, Album
from imager_profile.tests import UserFactory

# from django.db import models
# from django.test import SimpleTestCase
# from django.test.utils import isolate_apps

import factory
import faker

FAKE = faker.Faker()


# ==================== FACTORY ============================================== #


class PhotoFactory(factory.django.DjangoModelFactory):
    """Make test images."""

    class Meta:
        """Setup factory model."""

        model = Photo

    image = factory.django.ImageField(filename='/tmp/image.jpg')


class AlbumFactory(factory.django.DjangoModelFactory):
    """Make test albums."""

    class Meta:
        """Setup factory model."""

        model = Album


# ===================== PHOTO MODEL TESTS =================================== #

class PhotoTestCase(TestCase):
    """Images and album model test runner."""

    def setUp(self):
        """Setup for the test."""
        self.user = UserFactory.create()
        self.photo = PhotoFactory.create(
            user=self.user,
        )

    def test_photo_has_title_attribute(self):
        """The photo should have a title attribute."""
        self.photo.title = 'Photo title'
        self.assertEqual(self.photo.title, 'Photo title')

    def test_photo_id_exists(self):
        """The photo should have an id/primary key."""
        self.assertTrue(self.photo.id)

    def test_photo_is_instance_of_model(self):
        """The photo should be an instance of the Photo model."""
        self.assertIsInstance(self.photo, Photo)

    def test_photo_has_description(self):
        """Test photo title field."""
        self.photo.description = 'The photo description.'
        self.assertEqual(self.photo.description, 'The photo description.')
