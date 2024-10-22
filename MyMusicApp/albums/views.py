from django.forms import modelform_factory
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from MyMusicApp.albums.mixins import AlbumFormPlaceholderMixin
from MyMusicApp.albums.models import Album
from MyMusicApp.utils.mixins import ReadOnlyFormMixin
from MyMusicApp.utils.profile_helpers import get_profile


class AlbumCreateView(AlbumFormPlaceholderMixin, CreateView):
    model = Album
    fields = ["album_name", "artist", "genre", "description", "image_url", "price"]
    template_name = "albums/album-add.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        profile = get_profile()
        form.instance.owner = profile
        return super().form_valid(form)


class AlbumDetailsView(DetailView):
    model = Album
    template_name = "albums/album-details.html"


class AlbumEditView(UpdateView):
    model = Album
    template_name = "albums/album-edit.html"
    fields = ["album_name", "artist", "genre", "description", "image_url", "price"]
    success_url = reverse_lazy("index")


class AlbumDeleteView(ReadOnlyFormMixin, DeleteView):
    model = Album
    template_name = "albums/album-delete.html"
    success_url = reverse_lazy("index")
    form_class = modelform_factory(
        Album,
        fields=("album_name", "artist", "genre", "description", "image_url", "price"),
    )

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs



