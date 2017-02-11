"""Imager Url pattern."""

from django.conf.urls import url
from imager_profile.views import profile_view, public_profile_view


urlpatterns = [
    # url(r'^(?P<username>\w+)/$', profile_view, name='profile'),
    url(r'^$', profile_view, name='profile'),
    url(r'^(?P<username>\w+)/$', public_profile_view, name='public_profile'),
