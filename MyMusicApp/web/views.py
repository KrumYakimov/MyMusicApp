from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .mixins import ProfileFormPlaceholderMixin
from ..albums.models import Album
from ..profiles.models import Profile
from ..utils.profile_helpers import get_profile


class ProfileCreateView(ProfileFormPlaceholderMixin, CreateView):
    model = Profile
    fields = ['username', 'email', 'age']
    template_name = "web/home-no-profile.html"
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class IndexView(TemplateView):
    template_name = 'web/home-with-profile.html'

    def get(self, request, *args, **kwargs):
        profile = get_profile()
        if profile is None:
            return redirect('profile-create')

        albums = Album.objects.filter(owner=profile)
        return self.render_to_response({'albums': albums, 'profile_exists': True})
