from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView

from MyMusicApp.utils.profile_helpers import get_profile


class ProfileDetailView(DetailView):
    template_name = "profiles/profile-details.html"

    def get_object(self, queryset=None):
        return get_profile()


class ProfileDeleteView(DeleteView):
    template_name = "profiles/profile-delete.html"
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return get_profile()
