"""Imager Profile Tests."""

from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from imager_profile.models import ImagerProfile

import factory
# from random import random
# from faker import Faker

# fake = Faker()


# ==================== FACTORY ============================================== #


class UserFactory(factory.django.DjangoModelFactory):
    """Factory for building new user objects."""

    username = factory.Sequence(lambda n: "Bob {}".format(n))
    email = factory.LazyAttribute(
        lambda x: "{}@imager.com".format(x.username.replace(" ", ""))
    )

    class Meta:
        """Setup factory model."""

        model = User


# ================== USER/PROFILE TESTS ===================================== #


class ProfileTestCase(TestCase):
    """Profile model test runner."""

    def setUp(self):
        """Setup for the test."""
        self.users = [UserFactory.create() for i in range(20)]

    def test_profile_created(self):
        """Test that ImagerProfile object is created once user is saved."""
        self.assertTrue(ImagerProfile.objects.count() == 20)

    def test_model_string(self):
        """Ensure each models has a string representation in Django shell."""
        for i in range(20):
            self.assertEqual(self.users[i].username, str(self.users[i]))

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
        """Active model manager should return query set of active profiles."""
        query = ImagerProfile.active.all()
        self.assertIsInstance(query[0], ImagerProfile)

    def test_update_profile(self):
        """Test that a profile update also updates db."""
        # self.users[0].profile.bio = "This is mo betta."
        # query = User.objects.first()
        # self.assertTrue(
        #     query.profile.bio == "This is mo betta.")
        pass

    def test_inactive_users_have_inactive(self):
        """."""
        this_user = self.users[0]
        this_user.is_active = False
        this_user.save()
        self.assertTrue(
            ImagerProfile.active.count() == User.objects.count() - 1)

    def test_profile_is_active(self):
        """Test profile.is_active is active."""
        for i in range(20):
            user = self.users[i]
            self.assertTrue(user.is_active)

    def test_string_returns_profile_info(self):
        """Test if the string method returns matching profile info."""
        for i in range(20):
            user = str(self.users[i])
            self.assertTrue('Bob', '@imager.com' in user)

    def test_profile_is_active(self):
        """Test profile.is_active is active."""
        for i in range(20):
            user = self.users[i]
            self.assertTrue(user.is_active)

    def test_string_returns_profile_info(self):
        """Test if the string method returns matching profile info."""
        for i in range(20):
            user = str(self.users[i])
            self.assertTrue('Bob', '@imager.com' in user)

# =================== FRONT END TESTS ======================================= #


class ProfileFrontEndTests(TestCase):
    """Testing for front end tests."""

    def setUp(self):
        """."""
        self.client = Client()
        self.request = RequestFactory()

    def test_how_view_is_status_ok(self):
        """."""
        from imagersite.views import home_view
        # from imager_profile.views import home_view
        req = self.request.get("/potato")
        response = home_view(req)
        self.assertTrue(response.status_code == 200)

    def test_home_route_is_status_ok(self):
        """."""
        response = self.client.get("/")
        self.assertTrue(response.status_code == 200)

    def test_home_route_uses_right_templates(self):
        """."""
        response = self.client.get("/")
        self.assertTemplateUsed(response, "imagersite/home.html")

    def test_login_route_redirects(self):
        """Test login route redirects."""
        new_user = UserFactory.create()
        new_user.username = "potato_joe"
        new_user.set_password("tugboats")
        new_user.save()
        # import pdb; pdb.set_trace()
        response = self.client.post("/login/", {
            "username": new_user.username,
            "password": "tugboats"
        })
        self.assertTrue(response.status_code == 302)

    def test_login_route_redirects_to_homepage(self):
        """Test login route redirects to homepage."""
        new_user = UserFactory.create()
        new_user.username = "potato_joe"
        new_user.set_password("tugboats")
        new_user.save()
        # import pdb; pdb.set_trace()
        response = self.client.post("/login/", {
            "username": new_user.username,
            "password": "tugboats"
        }, follow=True)
        self.assertRedirects(
            response, "/", status_code=302, target_status_code=200
        )
