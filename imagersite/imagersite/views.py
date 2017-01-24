"""Views."""

from django.shortcuts import render

# Create your views here.


def home_view(request):
    """Home view."""
    return render(request, 'imagersite/home.html', {'foo': bar})
    # return render(request, 'imagersite/home.html')
