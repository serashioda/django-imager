from django.conf.urls import url

from imager_api.views import(
    APIUserPhotoListView,
    APIUserAlbumListView,
    APIAlbumPhotosView
)

app_name = 'imager_api'

urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/$', APIUserPhotoListView.as_view(), name="api_user_photo_list"),
    url(r'^(?P<username>[\w.@+-]+)/album/$', APIUserAlbumListView.as_view(), name="api_user_album_list"),
    url(r'^(?P<username>[\w.@+-]+)/album/(?P<id>[0-9]+)/$', APIAlbumPhotosView.as_view(), name="api_user_album_list")
]
