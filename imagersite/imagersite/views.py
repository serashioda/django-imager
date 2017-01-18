"""Sites root base."""

from django.shortcuts import render


# Create your views here.

def home_view(request):
    """The home view."""
    return render(request, "imagersite/base.html", {"": ""})
