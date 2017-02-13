"""Images url paths."""
from django.conf.urls import url, include
from imager_images.models import Album, Photo
from imager_images.views import AlbumView, PhotoView, AlbumCollectionView, PhotoCollectionView, LibraryView, AddAlbum, AddPhoto, EditAlbum, EditPhoto, TagListView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^photos/(?P<photo_id>\d+)', PhotoView.as_view(), name='show_photo'),
    url(r'^albums/(?P<album_id>\d+)', AlbumView.as_view(), name='show_album'),
    url(r'^library/$', LibraryView.as_view(), name='library'),
    url(r'^photos/add/$', AddPhoto.as_view(), name='add_photo'),
    url(r'^photos/(?P<pk>\d+)/edit/$', EditPhoto.as_view(), name='edit_photo'),
    url(r'^albums/add/$', AddAlbum.as_view(), name='add_album'),
    url(r'^albums/(?P<pk>\d+)/edit/$', EditAlbum.as_view(), name='edit_album'),
    url(r'^albums/$', AlbumCollectionView.as_view(), name='list_albums'),
    url(r'^photos/$', PhotoCollectionView.as_view(), name='list_photos'),
    url(r'^tagged/(?P<tag>[\w-]+)/$', TagListView.as_view(), name='tag_list'),
    url(r'', include('two_factor.urls', 'two_factor')),
]
