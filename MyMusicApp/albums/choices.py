from django.db import models


class MusicGenre(models.TextChoices):
    POP = "Pop Music", "Pop Music"
    JAZZ = "Jazz Music", "Jazz Music"
    RNB = "R&B Music", "R&B Music"
    ROCK = "Rock Music", "Rock Music"
    COUNTRY = "Country Music", "Country Music"
    DANCE = "Dance Music", "Dance Music"
    HIP_HOP = "Hip Hop Music", "Hip Hop Music"
    OTHER = "Other", "Other"

