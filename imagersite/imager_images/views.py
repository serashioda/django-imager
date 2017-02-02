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


class AddPhoto(PermissionRequiredMixin, CreateView):
    """Add photo."""

    login_url = reverse_lazy('login')
    permission_required = "imager_images.add_photo"

    template_name = "imager_images/add_photo.html"
    model = Photo
    fields = ['image', 'title', 'description', 'published']
    success_url = reverse_lazy('library')

    def form_valid(self, form):
        """Form validation for adding a photo."""
        form.instance.user = self.request.user
        return super(AddPhoto, self).form_valid(form)


class EditPhoto(PermissionRequiredMixin, UpdateView):
    """Edit photo."""

    permission_required = "imager_images.change_photo"

    template_name = "imager_images/add_photo.html"
    model = Photo
    fields = ['image', 'title', 'description']
    success_url = reverse_lazy('library')


class AddAlbum(PermissionRequiredMixin, CreateView):
    """Add album."""

    login_url = reverse_lazy('login')
    permission_required = "imager_images.add_album"

    template_name = "imager_images/add_album.html"
    model = Album
    fields = ['cover', 'title', 'description', 'photos']
    success_url = reverse_lazy('library')

    def form_valid(self, form):
        """Form validation for adding album."""
        form.instance.user = self.request.user
        return super(AddAlbum, self).form_valid(form)


class EditAlbum(PermissionRequiredMixin, UpdateView):
    """Edit Album."""

    permission_required = "imager_images.change_album"

    template_name = "imager_images/add_album.html"
    model = Album
    fields = ['title', "cover", "description", "photos"]
    success_url = reverse_lazy('library')
