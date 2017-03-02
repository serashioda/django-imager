"""Imager profile view."""
# from imager_profile.models import ImagerProfile
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView


class Profile(LoginRequiredMixin, ListView):
    """Profile view."""

    print('just mine')
    login_url = reverse_lazy('login')

    model = User
    template_name = "imager_profile/profile.html"

    # # profile = ImagerProfile.active.filter(user__username=username).first()
    # photos = request.user.photos.all().order_by('-id')
    # # import pdb; pdb.set_trace()
    # return render(request, 'imager_profile/profile.html', {'photos': photos})


class PublicProfile(ListView):
    """Public profile view."""

    print('public yo')
    # print('username:', username)

    model = User
    template_name = "imager_profile/profile.html"

    def get_context_data(self):
        """Return user object."""
        return {"user": User.objects.get(username=self.kwargs['username'])}

    # profile = ImagerProfile.active.filter(user__username=username).first()
    # photos = request.user.photos.all().order_by('-id')
    # return render(request, 'imager_profile/public_profile.html', {'profile': profile}, {'photos': photos})
