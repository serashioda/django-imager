"""Views."""

from django.shortcuts import render


def home_view(request):
    """Home view."""
    return render(request, 'imagersite/home.html')
    # return render(request, 'imagersite/home.html', {'foo': bar})
