"""Imager Url pattern."""

from django.conf.urls import url
from imager_profile import views

urlpatterns = [
    url(r'(?P<username>\w+)/$', views.profile_view, name='profile'),
]
