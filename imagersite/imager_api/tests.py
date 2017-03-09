"""Test API views."""
from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient
from django.contrib.auth.models import User
from imager_images.models import Photo, Album
from django.core.files.uploadedfile import SimpleUploadedFile


class PhotoTestCase(TestCase):
    """Images and album model test runner."""

    factory = APIRequestFactory()

    def test_api_user_photo_list(self):
        """Test the user API photo list."""
        user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
        photo = Photo()
        photo.user = user
        photo.image = SimpleUploadedFile(name='test_image.jpg', content=open('imagersite/static/images/bob.jpg', 'rb').read(), content_type='image/jpeg')
        photo.save()

        client = APIClient()
        client.login(username='temporary', password='temporary')
        response = client.get('/api/v1/temporary/')

        assert response.status_code == 200

        body = response.content.decode('utf-8')
        assert body != '[]'

        response = client.get('/api/v1/i_dont_exist/')
        assert response.status_code == 200
        body = response.content.decode('utf-8')
        assert body == '[]'

    def test_api_user_album_list(self):
        """Test the user API photo list."""
        user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
        photo = Photo()
        photo.user = user
        photo.image = SimpleUploadedFile(name='test_image.jpg', content=open('imagersite/static/images/bob.jpg', 'rb').read(), content_type='image/jpeg')
        photo.save()

        album = Album()
        album.title = 'rock'
        album.cover = photo
        album.user = user
        album.save()

        client = APIClient()
        client.login(username='temporary', password='temporary')
        response = client.get('/api/v1/temporary/album/')

        assert response.status_code == 200
        body = response.content.decode('utf-8')
        assert body != '[]'

        response = client.get('/api/v1/i_dont_exist/album/')
        assert response.status_code == 200
        body = response.content.decode('utf-8')
        assert body == '[]'

    def test_api_user_album_photos_list(self):
        """Test the user API photo list."""
        user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
        photo = Photo()
        photo.user = user
        photo.image = SimpleUploadedFile(name='test_image.jpg', content=open('imagersite/static/images/bob.jpg', 'rb').read(), content_type='image/jpeg')
        photo.save()

        album = Album()
        album.title = 'rock'
        album.cover = photo
        album.user = user
        album.save()

        client = APIClient()
        client.login(username='temporary', password='temporary')
        response = client.get('/api/v1/temporary/album/' + str(album.id) + '/')

        assert response.status_code == 200
        body = response.content.decode('utf-8')
        assert body == '[]'
