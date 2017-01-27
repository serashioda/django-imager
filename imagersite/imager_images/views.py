"""Views for images."""
from django.shortcuts import render
from imager_images.models import Photo, Album
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def single_photo(request, photo_id):
    """."""
    photo = Photo.objects.get(id=photo_id)
    if photo.published == 'private' and photo.user_id == request.user.id:
        return HttpResponse('Unauthorized', status=401)
    return render(request, 'imager_images/photo.html', {"photo": photo})


def all_photos(request):
    """."""


def single_album(request, album_id):
    """."""


def all_albums(request):
    """."""


@login_required(login_url='/accounts/login/')
def library(request):
    """Library view."""
