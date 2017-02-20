"""Imager Url pattern."""

from django.conf.urls import url
from imager_profile.views import Profile, PublicProfile, EditProfile


urlpatterns = [
    url(r'^edit/$', EditProfile.as_view(), name='edit_profile'),
    url(r'^(?P<username>\w+)/$', PublicProfile.as_view(), name='public_profile'),
    url(r'^$', Profile.as_view(), name='profile')
]
