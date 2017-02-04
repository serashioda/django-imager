"""Imager Url pattern."""

from django.conf.urls import url
from imager_profile.views import profile_view
# from imager_profile import views


urlpatterns = [
    url(r'(?P<username>\w+)/$', profile_view, name='profile'),
]
