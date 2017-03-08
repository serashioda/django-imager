"""Views for images."""
from django.core.paginator import(
    Paginator,
    EmptyPage,
    PageNotAnInteger
)

from django.http import HttpResponse
# from django.http import HttpResponseRedirect
# from django.http import HttpResponseForbidden

from django.urls import reverse_lazy

from django.views.generic.edit import CreateView
from django.views.generic import(
    ListView,
    # TemplateView,
    # CreateView,
    UpdateView
)

# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# from django.shortcuts import render
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
        all_album_photos = album.photos.all()
        for p in all_album_photos:
            for tag in p.tags.all():
                if tag not in tags:
                    tags.append(tag)

        photo_list = all_album_photos
        p_paginator = Paginator(photo_list, 4)
        p_page = self.request.GET.get('photo_page')

        try:
            photo_page = p_paginator.page(p_page)
        except PageNotAnInteger:
            photo_page = p_paginator.page(1)
        except EmptyPage:
            photo_page = p_paginator.page(p_paginator.num_pages)

        return {'album': album, 'photos': photo_page, 'tags': tags}


class PhotoView(ListView):
    """Photo View."""

    model = Photo
    template_name = 'imager_images/photo.html'

    def get_context_data(self):
        """Group photos with common tags."""
        photo = Photo.objects.get(id=self.kwargs.get('photo_id'))

        common_tag_photos = Photo.objects.filter(
            tags__in=photo.tags.all()
        ).exclude(
            id=self.kwargs.get("photo_id")
        ).distinct()

        if photo.published == 'private' and photo.user.username != self.request.user.username:
            return HttpResponse('Unauthorized, status=401')
        return {'photo': photo, 'tag_photos': common_tag_photos[:5]}


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
        user = self.request.user
        albums = user.albums.all().order_by('-id')
        photos = user.photos.all().order_by('-id')
        tag_list = Photo.tags.all()

        photo_list = Photo.objects.all()
        p_paginator = Paginator(photo_list, 4)
        p_page = self.request.GET.get('photo_page')

        try:
            photo_page = p_paginator.page(p_page)
        except PageNotAnInteger:
            photo_page = p_paginator.page(1)
        except EmptyPage:
            photo_page = p_paginator.page(p_paginator.num_pages)

        album_list = Album.objects.all()
        a_paginator = Paginator(album_list, 4)
        a_page = self.request.GET.get('album_page')

        try:
            album_page = a_paginator.page(a_page)
        except PageNotAnInteger:
            album_page = a_paginator.page(1)
        except EmptyPage:
            album_page = a_paginator.page(a_paginator.num_pages)

        return {"albums": album_page, "photos": photo_page, "tags": tag_list}

        # return {'photos': photos, 'albums': albums, 'tags': tag_list}

    def get_queryset(self):
        """."""
        return {}


class AddPhoto(LoginRequiredMixin, CreateView):
    """Add photo."""

    login_url = reverse_lazy('login')

    template_name = "imager_images/add_photo.html"
    model = Photo

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

    template_name = "imager_images/add_album.html"
    model = Album
    fields = ['cover', 'title', 'description', 'photos', 'published']
    success_url = reverse_lazy('library')
    # login_url = reverse_lazy('login')

    def form_valid(self, form):
        """Form validation for adding album."""
        form.instance.user = self.request.user
        return super(AddAlbum, self).form_valid(form)


class EditAlbum(LoginRequiredMixin, UpdateView):
    """Edit Album."""

    template_name = "imager_images/add_album.html"
    model = Album

    fields = ['title', 'cover', 'description', 'photos']
    success_url = reverse_lazy('library')


class TagListView(ListView):
    """Listing for tagged photos."""

    template_name = 'imager_images/user_tag_list.html'
    slug_field_name = 'tag'

    def get_queryset(self):
        """."""
        return Photo.objects.filter(tags__slug=self.kwargs.get('slug')).all()

    def get_context_data(self, **kwargs):
        """."""
        context = super(TagListView, self).get_context_data(**kwargs)
        context['tag'] = self.kwargs.get('slug')
        context['photos'] = Photo.objects.filter(tags__slug=self.kwargs.get('slug')).all()
        return context
