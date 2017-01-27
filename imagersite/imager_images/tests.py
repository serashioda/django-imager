"""Tests for imager_images app."""

from django.test import TestCase
from django.contrib.auth.models import User
from imager_images.models import Photo, Album

# from django.db import models
# from django.test import SimpleTestCase
# from django.test.utils import isolate_apps

import factory


# Create your tests here.
#  -- example test ---
# @isolate_apps('app_label', attr_name='apps')
# class TestModelDefinition(SimpleTestCase):
#     """."""

#     def test_model_definition(self):
#         """."""
#         class TestModel(models.Model):
#             pass
#         self.assertIs(self.apps.get_model(
#             'app_label', 'TestModel'), TestModel)


class ImageTestCase(TestCase):
    """Images and album model test runner."""

    class UserFactory(factory.django.DjangoModelFactory):
        """Make test users."""

        class Meta:
            """Setup factory model."""

            model = User
        username = factory.Sequence(lambda n: "Bob {}".format(n))
        email = factory.LazyAttribute(
            lambda x: "{}@imager.com".format(x.username.replace(" ", ""))
        )

    class PhotoFactory(factory.django.DjangoModelFactory):
        """Make test images."""

        class Meta:
            """Setup factory model."""

            model = Photo
        title = factory.Sequence(lambda n: "Photo {}".format(n))

    class AlbumFactory(factory.django.DjangoModelFactory):
        """Make test albums."""

        class Meta:
            """Setup factory model."""

            model = Album
        title = factory.Sequence(lambda n: "Album {}".format(n))

    def setUp(self):
        """Setup for the test."""
        self.users = [self.UserFactory.create() for i in range(20)]
        self.photos = [self.PhotoFactory.create() for i in range(120)]
        self.albums = [self.AlbumFactory.create() for i in range(40)]

    # def test_that_photo_has_title(self):
    #     """Test that the photo has a title."""
    #     self.assertTrue("Photo" in Photo.objects.first().title)
