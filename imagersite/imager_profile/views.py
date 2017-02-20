"""Imager profile view."""
# from imager_profile.models import ImagerProfile
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView


class Profile(LoginRequiredMixin, ListView):
    """Profile view."""

    login_url = reverse_lazy('login')

    model = User
    template_name = "imager_profile/profile.html"


class PublicProfile(ListView):
    """Public profile view."""

    model = User
    template_name = "imager_profile/profile.html"

    def get_context_data(self):
        """Return user object."""
        import pdb; pdb.set_trace()
        return {"user": User.objects.get(username=self.kwargs['username'])}


class EditProfile(UpdateView):
    """Edit user profile."""

    login_url = reverse_lazy('login')
    permission_required = "imager_images.change_profile"

    model = User
    template_name = "imager_profile/edit_profile.html"

    fields = ['bio', 'personal_website', 'hireable', 'address', 'phone', 'travel_radius', 'camera_type', 'photo_type']
    success_url = reverse_lazy('profile')

    def get_context_data(self):
        """."""
        import pdb; pdb.set_trace()
        return self.request.user.profile
