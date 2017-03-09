"""Imager Profile Tests."""
from django.test import TestCase
from django.contrib.auth.models import User
from imagersite.views import home_view
from imager_images.models import Photo
from django.core.urlresolvers import reverse
from django.core.files.uploadedfile import SimpleUploadedFile


class ImagerSiteHomeTestCase(TestCase):
    """Test the home view."""

    def test_home_view(self):
        """Test that the home view doesn't explode."""
        user = User()
        user.username = 'billybob'
        user.save()

        photo = Photo()
        photo.user = user
        photo.published = 'public'
        photo.image = SimpleUploadedFile(name='test_image.jpg', content=open('imagersite/static/images/bob.jpg', 'rb').read(), content_type='image/jpeg')
        photo.save()

        response = self.client.get(reverse('home'))
        assert(response.status_code == 200)
