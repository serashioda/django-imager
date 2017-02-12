"""Imager Url pattern."""

from django.conf.urls import url
from imager_profile.views import Profile, PublicProfile


urlpatterns = [
    # url(r'^(?P<username>\w+)/$', profile_view, name='profile'),
    url(r'^$', Profile.as_view(), name='profile'),
    url(r'^(?P<username>\w+)/$', PublicProfile.as_view(), name='public_profile')
]


# from django.conf.urls import url
# from .views import Profile, PublicProfile
# from django.contrib.auth.decorators import login_required

# urlpatterns = [
#     url(r'^(?P<username>\w+)', PublicProfile.as_view(), name='public_profile'),
#     url(r'^$', login_required(Profile.as_view()), name='private_profile')
# ]
