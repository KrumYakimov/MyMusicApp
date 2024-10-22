from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from .models import Song


from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Song


class SongCreateView(CreateView):
    model = Song
    fields = ['song_name', 'album']
    template_name = 'songs/create-song.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        music_file = self.request.FILES.get('music_file')
        form.instance.music_file_data = music_file.read()
        return super().form_valid(form)


class SongServeView(DetailView):
    model = Song

    def render_to_response(self, context, **response_kwargs):
        song = self.get_object()  # Get the song object from the database

        # Serve the binary file as a response
        response = HttpResponse(song.music_file_data, content_type="audio/mpeg")
        response["Content-Disposition"] = f'inline; filename="{song.song_name}"'
        return response


class SongPlayView(DetailView):
    model = Song
    template_name = "songs/music-player.html"
    context_object_name = "song"

    def get_object(self, queryset=None):
        # If you need a custom query, you can define it here
        return super().get_object(queryset)



