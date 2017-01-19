"""Imager profile view."""
from django.shortcuts import render
from imager_profile.models import ImagerProfile

# Create your views here.


def profile_view(request, username):
    """Profile view."""
    profile = ImagerProfile.active.filter(user__username=username).first()
    photos = profile.photos.all()
    return render(request, 'imager_profile/profile.html', {'photos': photos})
