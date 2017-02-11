"""Imager profile view."""
from django.shortcuts import render
from imager_profile.models import ImagerProfile


def profile_view(request):
    """Profile view."""
    print('just mine')
    # profile = ImagerProfile.active.filter(user__username=username).first()
    photos = request.user.photos.all().order_by('-id')
    return render(request, 'imager_profile/profile.html', {'photos': photos})


def public_profile_view(request, username):
    """Public profile view."""
    print('public yo')
    print('username:', username)
    profile = ImagerProfile.active.filter(user__username=username).first()
    photos = request.user.photos.all().order_by('-id')
    return render(request, 'imager_profile/public_profile.html', {'profile': profile}, {'photos': photos})
