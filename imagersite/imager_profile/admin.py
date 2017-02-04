<<<<<<< HEAD
"""Admin model registration."""

from django.contrib import admin
from imager_profile.models import ImagerProfile


# Register your models here.

=======
"""Register models."""

from django.contrib import admin
from imager_profile.models import ImagerProfile

>>>>>>> df061446c8ef235667945a254571b871ad0c3668
admin.site.register(ImagerProfile)
