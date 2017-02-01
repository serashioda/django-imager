"""Views for images."""
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseForbidden

from django.urls import reverse
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView
from django.views.generic import ListView, TemplateView

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from imager_images.models import Photo, Album


class AlbumView(ListView):
    """Album View."""

    template_name = 'imager_images/album.html'
    model = Album

    def get_context_data(self):
        """."""
        album = Album.objects.get(id=self.kwargs['album_id'])
        if album.published == 'private' and album.user.username != request.user.username:
            return HttpResponse('Unauthorized, status=401')
        return {'album': album}


class PhotoView(ListView):
    """Photo View."""

    template_name = 'imager_images/photo.html'
    model = Photo

    def get_context_data(self):
        """."""
        album = Photo.objects.get(id=self.kwargs['photo_id'])
        if photo.published == 'private' and photo.user.username != request.user.username:
            return HttpResponse('Unauthorized, status=401')
        return {'photo': photo}


class PhotoCollectionView(ListView):
    """Photo View."""

    template_name = 'imager_images/photos.html'

    def get_context_data(self):
        """."""
        public_photos = []
        photos = Photo.objects.all()
        for photo in photos:
            if photo.published != 'private' or photo.user.username == self.request.user.username:
                public_photos.append(photo)
        return {'photos': public_photos}

    def get_queryset(self):
        """."""
        return {}


class AlbumCollectionView(ListView):
    """Album collections view."""

    template_name = 'imager_images/albums.html'

    def get_context_data(self):
        """."""
        public_albums = []
        albums = Album.objects.all()
        for album in albums:
            if album.published != 'private' and album.user.username == self.request.user.username:
                public_albums.append(album)
        return {'albums': public_albums}

    def get_queryset(self):
        """."""
        return {}


class LibraryView(ListView):
    """Library View."""

    template_name = 'imager_images/library.html'

    def get_context_data(self):
        """Library view."""
        albums = self.request.user.albums.all()
        photos = self.request.user.photos.all()
        return {'photos': photos, 'albums': albums}

    def get_queryset(self):
        """."""
        return {}

class AddPhoto(CreateView):
    """Add a photo."""

    template_name = "imager_images/add_photo.html"
    model = Photo
    fields = ['image', 'title', 'description', 'published']
    success_url = reverse_lazy('library')

    def form_valid(self, form):
        """."""
        form.instance.user = self.request.user
        return super(AddPhoto, self).form_valid(form)


class AddAlbum(CreateView):
    """Add album."""

    template_name = "imager_images/add_album.html"
    model = Album
    fields = ['cover', 'title', 'description', 'photos']
    success_url = reverse_lazy('library')

    def form_valid(self, form):
        """."""
        form.instance.user = self.request.user
        return super(AddAlbum, self).form_valid(form)

# @login_required(login_url='/accounts/login/')
# def library(request):
#     """Library view."""
#     albums = request.user.albums.all()
#     photos = request.user.photos.all()
#     return render(
#         request,
#         'imager_images/library.html',
#         context={'albums': albums, 'photos': photos}
#     )


# def single_photo(request, photo_id):
#     """."""
#     photo = Photo.objects.get(id=photo_id)
#     if photo.published == 'private' and photo.user_id != request.user.id:
#         return HttpResponse('Unauthorized', status=401)
#     return render(request, 'imager_images/photo.html', {"photo": photo})


# def all_photos(request):
#     """."""
#     public_photos = []
#     photos = Photo.objects.all()
#     for photo in photos:
#         if photo.published != 'private' or photo.user.username == request.user.username:
#             public_photos.append(photo)
#     return render(
#         request,
#         'imager_images/photos.html',
#         {'photos': public_photos}
#     )


# def single_album(request, album_id):
#     """."""
#     # import pdb; pdb.set_trace()
#     album = Album.objects.get(id=album_id)
#     if album.published == 'private' and album.user.username != request.user.username:
#         return HttpResponse('Unauthorized, status=401')
#     return render(
#         request,
#         'imager_images/album.html',
#         {'album': album}
#     )


# def all_albums(request):
#     """."""
#     public_albums = []
#     albums = Album.objects.all()
#     for album in albums:
#         if album.published != 'private' and album.user.username == request.user.username:
#             public_albums.append(album)
#     return render(
#         request,
#         'imager_images/albums.html',
#         {'albums': public_albums}
#     )
