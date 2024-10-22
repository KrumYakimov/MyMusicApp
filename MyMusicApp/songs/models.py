from django.db import models


class Song(models.Model):
    MAX_SONG_NAME_LENGTH = 140

    song_name = models.CharField(
        max_length=MAX_SONG_NAME_LENGTH,
        null=False,
        blank=False
    )

    music_file_data = models.BinaryField(
        null=False,
        blank=False
    )

    album = models.ForeignKey(
        'albums.Album',
        on_delete=models.CASCADE,
        related_name='songs'
    )

    def __str__(self):
        return self.song_name
