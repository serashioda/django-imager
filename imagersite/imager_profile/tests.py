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
        email = factory.LazyAttribute(
            lambda x: "{}@imager.com".format(x.username.replace(" ", ""))
        )

    def setUp(self):
        """Setup for the test."""
        self.users = [self.UserFactory.create() for i in range(20)]

    def test_profile_created(self):
        """Test that profile is created once user is saved."""
        self.assertTrue(ImagerProfile.objects.count() == 20)

    def test_model_string(self):
        """Ensure each models has a string representation that
        appropriately displays when using the Django shell.
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

    def test_user_associated_with_profile(self):
        """Ensure that profile is associated with appropriate user."""
        profile = ImagerProfile.objects.first()
        self.assertTrue(hasattr(profile, 'user'))
        self.assertIsInstance(profile.user, User)

    def test_model_manager_returns_active_profiles(self):
        """Test that active model manager returns query set of active profiles."""
        query = ImagerProfile.active.all()
        self.assertIsInstance(query[0], ImagerProfile)

    def test_update_profile(self):
        """Test that a profile update also updates db."""
        user = self.users[0]
        user.profile.bio = "I am updating my bio because this is mo betta."
        query = User.objects.first()
        self.assertTrue(query.profile.bio == "I am updating my bio because this is mo betta.")

    def test_del_user_on_db_and_profile(self):
        """Test delete user on DB & Imgr.

        Ensure that if a user is deleted from the database, the ImagerProfile
        associated with that user is also deleted.
        """
        pass

    # def test_profile_is_active(self):
    #     """Test profile.is_active is active."""
    #     for i in range(20):
    #         user = self.users[i]
    #         # self.assertTrue(user.is_active)
