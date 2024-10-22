from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from MyMusicApp.albums.choices import MusicGenre


class Album(models.Model):
    MAX_ALBUM_NAME_LENGTH = 30
    MAX_ARTIST_LENGTH = 30
    MAX_GENRE_LENGTH = 30

    MIN_PRICE = 0.0

    album_name = models.CharField(
        max_length=MAX_ALBUM_NAME_LENGTH,
        unique=True,
        null=False,
        blank=False,
        verbose_name="Album Name"
    )
    artist = models.CharField(
        max_length=MAX_ARTIST_LENGTH,
        null=False,
        blank=False,
        verbose_name="Artist"

    )

    genre = models.CharField(
        max_length=MAX_GENRE_LENGTH,
        choices=MusicGenre.choices
    )

    description = models. TextField(
        null=True,
        blank=True
    )

    image_url = models.URLField(
        null=False,
        blank=False
    )

    price = models.FloatField(
        validators=[
            MinValueValidator(MIN_PRICE)
        ],
        null=False,
        blank=False
    )

    owner = models.ForeignKey(
        "profiles.Profile",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.album_name
