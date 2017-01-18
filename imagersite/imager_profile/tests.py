"""Imager Profile Tests."""

from django.test import TestCase
from django.contrib.auth.models import User
from imager_profile.models import ImagerProfile
import factory

# Create your tests here.


class ProfileTestCase(TestCase):
    """Profile model test runner."""

    class UserFactory(factory.django.DjangoModelFactory):
        """Factory for building new user objects."""

        class Meta:
            """Setup factory model."""

            model = User

        username = factory.Sequence(lambda n: "Pho To Combo {}".format(n))

    def setUp(self):
        """Setup for the test."""
        self.users = [self.UserFactory.create() for i in range(20)]

    def test_model_string(self):
        """String.

        Ensure that each of your models has a string representation that
        appropriately displays it when using the Django shell.
        """
        for i in range(20):
            self.assertIs(self.users[i].username, str(self.users[i]))

    def test_user_gets_imgr_profile(self):
        """Test User gets Imager Profile.

        Ensure that every standard Django user object created automatically
        gets an ImagerProfile.
        """
        for i in range(20):
            user = self.users[i]
            self.assertTrue(hasattr(user, 'profile'))
            self.assertIsInstance(user.profile, ImagerProfile)

    def test_del_user_on_db_and_profile(self):
        """Test delete user on DB & Imgr.

        Ensure that if a user is deleted from the database, the ImagerProfile
        associated with that user is also deleted.
        """
        pass

    def test_imager_profile_is_active(self):
        """Test profile is active."""
        pass

    def test_profile_is_active_is_active(self):
        """Test profile.is_active is active."""
        for i in range(20):
            user = self.users[i]
            # self.assertTrue(user.is_active)
