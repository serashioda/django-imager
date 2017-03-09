"""Tests for imager_images app."""
from django.test import TestCase
from imager_images.views import get_page_size
from imager_images.models import Photo, Album
from imager_profile.tests import UserFactory
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

import faker
import factory

FAKE = faker.Faker()

# ==================== FACTORY ============================================== #


class RequestFactory():
    """Stub that fakes a request."""

    GET = {}
    session = {}


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

    def test_photo_constructor(self):
        """Test that the photo constructor works properly."""
        u = User()
        u.save()
        p = Photo()
        p.title = "foo"
        p.user = u
        p.description = "rubber duckies"
        p.save()
        assert p is not None
        assert str(p) is not None

        users = User.objects.all()
        assert users is not None
        for user in users:
            assert user.username is not None

        photos = Photo.objects.all()
        assert photos is not None
        for photo in photos:
            assert photo.title is not None

    def test_photo_is_instance_of_model(self):
        """The photo should be an instance of the Photo model."""
        self.assertIsInstance(self.photo, Photo)

    def test_photo_has_description(self):
        """Test photo title field."""
        self.photo.description = 'The photo description.'
        self.assertEqual(self.photo.description, 'The photo description.')

    def test_photo_can_be_assigned_to_user(self):
        """Test that a photo is linked to a user."""
        mongo = self.user
        mongo.username = "Mongo the doge"
        mongo.save()
        doge_photo = Photo(user=mongo)
        doge_photo.save()
        self.assertTrue(doge_photo.user.username == mongo.username)

    def test_page_size(self):
        """Test that the page function returns the correct results."""
        request = RequestFactory()

        size = get_page_size(request)
        assert(size == 4)

        request.GET['page_size'] = 10
        size = get_page_size(request)
        assert(size == 10)

        request = RequestFactory()
        request.session['page_size'] = 10
        size = get_page_size(request)
        assert(size == 10)

    def test_photo_collection_view(self):
        """Test photo collection view."""
        user = User()
        user.username = 'billybob'
        user.save()

        for i in range(0, 10):
            photo = Photo()
            photo.user = user
            photo.image = SimpleUploadedFile(name='test_image.jpg', content=open('imagersite/static/images/bob.jpg', 'rb').read(), content_type='image/jpeg')
            photo.save()
        response = self.client.get(reverse('list_photos'))
        assert(response.status_code == 200)

    def test_album_collection_view(self):
        """Test photo collection view."""
        user = User()
        user.username = 'billybob'
        user.save()

        photo = Photo()
        photo.user = user
        photo.image = SimpleUploadedFile(name='test_image.jpg', content=open('imagersite/static/images/bob.jpg', 'rb').read(), content_type='image/jpeg')
        photo.save()

        for i in range(0, 10):
            album = Album()
            album.user = user
            album.cover = photo
            album.save()

        response = self.client.get(reverse('list_albums'))
        assert(response.status_code == 200)

    def test_tag_collection_view(self):
        """Test tag collection view."""
        user = User()
        user.username = 'billybob'
        user.save()

        for i in range(0, 10):
            photo = Photo()
            photo.user = user
            photo.image = SimpleUploadedFile(name='test_image.jpg', content=open('imagersite/static/images/bob.jpg', 'rb').read(), content_type='image/jpeg')
            photo.save()
            photo.tags.add('bar')
            photo.save()

        response = self.client.get(reverse('tag_list', kwargs={'tag': 'bar'}))
        assert(response.status_code == 200)

    def test_album_view(self):
        """Test that the album view doesn't explode."""
        user = User()
        user.username = 'billybob'
        user.save()

        photo = Photo()
        photo.user = user
        photo.save()

        album = Album()
        album.title = 'rock'
        album.cover = photo
        album.user = user
        album.save()

        response = self.client.get(reverse('show_album', kwargs={'album_id': album.id}))
        assert(response.status_code == 200)

    def test_photo_view(self):
        """Test that the photo view doesn't explode."""
        user = User()
        user.username = 'billybob'
        user.save()

        photo = Photo()
        photo.user = user
        photo.image = SimpleUploadedFile(name='test_image.jpg', content=open('imagersite/static/images/bob.jpg', 'rb').read(), content_type='image/jpeg')
        photo.save()

        response = self.client.get(reverse('show_photo', kwargs={'photo_id': photo.id}))
        assert(response.status_code == 200)

    def test_library_view(self):
        """Test that the library view works."""
        user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
        self.client.login(username='temporary', password='temporary')

        photo = Photo()
        photo.user = user
        photo.image = SimpleUploadedFile(name='test_image.jpg', content=open('imagersite/static/images/bob.jpg', 'rb').read(), content_type='image/jpeg')
        photo.save()

        album = Album()
        album.title = 'rock'
        album.cover = photo
        album.user = user
        album.save()

        response = self.client.get(reverse('library'))
        assert(response.status_code == 200)


# =========================================================================== #
