"""Views for images."""
from django.shortcuts import render
from imager_images.models import Photo, Album
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def single_photo(request, photo_id):
    """."""
    photo = Photo.objects.get(id=photo_id)
    if photo.published == 'private' and photo.user_id != request.user.id:
        return HttpResponse('Unauthorized', status=401)
    return render(request, 'imager_images/photo.html', {"photo": photo})


def all_photos(request):
    """."""
    public_photos = []
    photos = Photo.objects.all()
    for photo in photos:
        if photo.published == 'private' and photo.user.username != request.user.username:
            return render(
                request,
                'imager_images/photos.html',
                {'photos': public_photos}
            )
    public_photos.append(photo)


def single_album(request, album_id):
    """."""
    album = Album.objects.get(id=album_id)
    if album.published == 'private' and album.user.username != request.user.username:
        return HttpResponse('Unauthorized, status=401')
    return render(
        request,
        'imager_images/album.html',
        {'album': album}
    )


def all_albums(request):
    """."""
    public_albums = []
    albums = Album.object.all()
    for album in albums:
        if album.published == 'private' and album.user.username != request.user.username:
            return render(
                request,
                'imager_images/albums.html',
                {'albums': public_albums})
    public_albums.append(album)


@login_required(login_url='/accounts/login/')
def library(request):
    """Library view."""
    albums = request.user.albums.all()
    photos = request.user.photos.all()
    return render(
        request,
        'imager_images/library.html',
        context={'albums': albums, 'photos': photos}
    )
