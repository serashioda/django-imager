"""Views."""

from django.shortcuts import render
from imager_images.models import Photo
import random

# Create your views here.


def home_view(request):
    """Home view."""
    public_photos = []
    photos = Photo.objects.all()
    for photo in photos:
        if (photo.published != 'private' or
                photo.user.username == request.user.username):
            public_photos.append(photo)
    idx = random.randint(0, (len(public_photos) - 1))
    photo = public_photos[idx]
    return render(request, 'imagersite/home.html', {"photo": photo})
