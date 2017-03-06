"""Views for imager_api."""

from django.contrib.auth.models import User
from django.core import serializers
import json
from imager_images.models import Photo, Album
from imager_api.serializers import PhotoSerializer
from rest_framework import mixins
from rest_framework import generics
from django.http import HttpResponse
from django.conf import settings
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class APIUserPhotoListView(mixins.ListModelMixin, generics.GenericAPIView):
    """Class based view to return list of photos for a user."""
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None, username=None):
        """Provide list of photos for a user."""
        try:
            user = User.objects.get(username=username)
        except:
            return HttpResponse("[]", content_type="application/json")

        photos = Photo.objects.filter(user=user)
        for photo in photos:
            photo.image = settings.MEDIA_URL + str(photo.image)

        return HttpResponse(serializers.serialize("json", photos), content_type="application/json")


class APIUserAlbumListView(mixins.ListModelMixin, generics.GenericAPIView):
    """Class based view to return list of photos for a user."""
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None, username=None):
        """Provide list of photos for a user."""
        try:
            user = User.objects.get(username=username)
        except:
            return HttpResponse("[]", content_type="application/json")

        albums = Album.objects.filter(user=user)
        res = []
        for album in albums:
            row = {}
            row['photos_url'] = '/api/v1/' + username + '/album/' + str(album.pk)
            row['cover_photo_id'] = album.cover.pk
            row['title'] = album.title
            row['description'] = album.description
            row['date_created'] = str(album.date_created)
            row['date_modified'] = str(album.date_modified)
            row['date_published'] = str(album.date_published)
            row['published'] = str(album.published)
            res.append(row)

        return HttpResponse(json.dumps(res), content_type="application/json")


class APIAlbumPhotosView(mixins.ListModelMixin, generics.GenericAPIView):
    """Class based view to return list of photos for a user."""
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None, username=None, id=None):
        """Provide list of photos for a user."""
        try:
            user = User.objects.get(username=username)
        except:
            return HttpResponse("[]", content_type="application/json")

        try:
            album = Album.objects.get(id=id,user=user)
        except:
            return HttpResponse("[]", content_type="application/json")

        photos = album.photos.all()
        for photo in photos:
            photo.image = settings.MEDIA_URL + str(photo.image)
        return HttpResponse(serializers.serialize("json", photos), content_type="application/json")
