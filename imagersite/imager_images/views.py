"""Views for images."""
from django.shortcuts import render
from imager_images.models import Photo, Album
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def single_photo(request, photo_id):
    """Return a single photo and it's meta-data."""
    photo = Photo.objects.get(id=photo_id)
    if photo.published == 'private' and photo.user_id != request.user.id:
        return HttpResponse('Unauthorized', status=401)
    return render(request, 'imager_images/photo.html', {"photo": photo})


def all_photos(request):
    """Return all public photos."""
    public_photos = []
    photos = Photo.objects.all().order_by('-id')
    for photo in photos:
        if (photo.published != 'private' or
                photo.user.username == request.user.username):
            public_photos.append(photo)
    return render(
        request,
        'imager_images/photos.html',
        {'photos': public_photos}
    )


def single_album(request, album_id):
    """Return a single album and it's contents."""
    album = Album.objects.get(id=album_id)
    if (album.published == 'private' and
            album.user.username != request.user.username):
        return HttpResponse('Unauthorized, status=401')
    return render(
        request,
        'imager_images/album.html',
        {'album': album}
    )


def all_albums(request):
    """Return all public albums."""
    public_albums = []
    albums = Album.objects.all()
    for album in albums:
        if (album.published != 'private' or
                album.user.username == request.user.username):
            public_albums.append(album)
    return render(
        request,
        'imager_images/albums.html',
        {'albums': public_albums}
    )


@login_required(login_url='/accounts/login/')
def library(request):
    """Return user submitted albums and photos."""
    albums = request.user.albums.all().order_by('-id')
    photos = request.user.photos.all().order_by('-id')
    return render(
        request,
        'imager_images/library.html',
        context={'albums': albums, 'photos': photos}
    )
