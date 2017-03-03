"""Views for imager_api."""


from imager_images.models import Photo
from imager_api.serializers import PhotoSerializer
from rest_framework import mixins
from rest_framework import generics


class APIUserPhotoListView(mixins.ListModelMixin, generics.GenericAPIView):
    """Class based view to return list of photos for a user."""

    serializer_class = PhotoSerializer
    # permission_classes = (permissions.IsAuthenticated, Owner)

    def get_queryset(self):
        """Provide list of photos for a user."""
        return Photo.objects.filter(user=self.request.user)
