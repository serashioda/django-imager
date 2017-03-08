"""Views for images."""
from django.http import HttpResponse
# from django.http import HttpResponseRedirect
# from django.http import HttpResponseForbidden

from django.urls import reverse_lazy

from django.views.generic.edit import CreateView
from django.views.generic import ListView, TemplateView, CreateView, UpdateView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render
from imager_images.models import Photo, Album


class AlbumView(ListView):
    """Album View."""

    model = Album
    template_name = 'imager_images/album.html'

    def get_context_data(self):
        """."""
        album = Album.objects.get(id=self.kwargs['album_id'])
        if album.published == 'private' and album.user.username != self.request.user.username:
            return HttpResponse('Unauthorized, status=401')

        tags = []
        for p in album.photos.all():
            for tag in p.tags.all():
                if tag not in tags:
                    tags.append(tag)

        return {'album': album, 'tags': tags}


class PhotoView(ListView):
    """Photo View."""

    model = Photo
    template_name = 'imager_images/photo.html'

    def get_context_data(self):
        """."""
        photo = Photo.objects.get(id=self.kwargs['photo_id'])

        if photo.published == 'private' and photo.user.username != self.request.user.username:
            return HttpResponse('Unauthorized, status=401')
        return {'photo': photo, 'tag_photos': context['tag_photos']}


class PhotoCollectionView(ListView):
    """Photo View."""

    template_name = 'imager_images/photos.html'

    def get_context_data(self):
        """."""
        public_photos = []
        photos = Photo.objects.all().order_by('-id')
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
            if album.published != 'private' or album.user.username == self.request.user.username:
                public_albums.append(album)
        return {'albums': public_albums}

    def get_queryset(self):
        """."""
        return {}


class LibraryView(ListView):
    """Library View."""

    login_url = reverse_lazy('login')

    template_name = 'imager_images/library.html'

    def get_context_data(self):
        """Library view."""
        albums = self.request.user.albums.all().order_by('-id')
        photos = self.request.user.photos.all().order_by('-id')
        return {'photos': photos, 'albums': albums}

    def get_queryset(self):
        """."""
        return {}


class AddPhoto(LoginRequiredMixin, CreateView):
    """Add photo."""

    login_url = reverse_lazy('login')

    model = Photo

    # template_name = "imager_images/add_photo.html"

    fields = ['image', 'title', 'description', 'published', 'tags']
    success_url = reverse_lazy('library')

    def form_valid(self, form):
        """Form validation for adding a photo."""
        form.instance.user = self.request.user
        return super(AddPhoto, self).form_valid(form)


class EditPhoto(LoginRequiredMixin, UpdateView):
    """Edit photo."""

    template_name = "imager_images/add_photo.html"
    model = Photo
    fields = ['image', 'title', 'description', 'tags']

    success_url = reverse_lazy('library')


class AddAlbum(LoginRequiredMixin, CreateView):
    """Add album."""

    # login_url = reverse_lazy('login')

    template_name = "imager_images/add_album.html"
    model = Album

    fields = ['cover', 'title', 'description', 'photos', 'published']
    success_url = reverse_lazy('library')

    def form_valid(self, form):
        """Form validation for adding album."""
        form.instance.user = self.request.user
        return super(AddAlbum, self).form_valid(form)


class EditAlbum(LoginRequiredMixin, UpdateView):
    """Edit Album."""

    model = Album
    template_name = "imager_images/add_album.html"

    fields = ['title', "cover", "description", "photos"]
    success_url = reverse_lazy('library')
