"""Serializers for RESTful API to expose user’s photos."""
from rest_framework import serializers
from imager_images.models import Photo, Album


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Photo object."""

    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Photo
        fields = (
            'user',
            'image',
            'title',
            'description',
            'date_uploaded',
            'date_published',
            'published'
        )


class AlbumSerializer(serializers.Serializer):
    """Define serializer for album data."""

    user = serializers.ReadOnlyField(source='user.username')
    photos = PhotoSerializer(many=True)

    class Meta:
        model = Album
        fields = (
            'user',
            'cover',
            'description',
            'date_created',
            'date_published'
            'published',
            'photos'
        )
