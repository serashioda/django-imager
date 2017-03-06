"""Imager profile view."""
from django.shortcuts import render
from imager_profile.models import ImagerProfile


def profile_view(request, username):
    """Profile view."""
    profile = ImagerProfile.is_active.filter(user__username=username).first()
    return render(request, 'imager_profile/profile.html')
