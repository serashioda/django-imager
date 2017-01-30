"""Images url paths."""
from django.conf.urls import url
from .views import single_photo, all_photos, single_album, all_albums, library

urlpatterns = [
    url(r'^photos/(?P<photo_id>\d+)', single_photo, name='show_photo'),
    url(r'^photos/$', all_photos, name='list_photos'),
    url(r'^albums/(?P<album_id>\d+)', single_album, name='show_album'),
    url(r'^albums/?', all_albums, name='list_albums'),
    url(r'^library$', library, name='library'),
]
