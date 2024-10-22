from django.core.validators import MinLengthValidator
from django.db import models

from MyMusicApp.profiles.validators import UserNameValidator


class Profile(models.Model):
    MIN_USERNAME_LENGTH = 2
    MAX_USERNAME_LENGTH = 15

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        validators=[
            MinLengthValidator(MIN_USERNAME_LENGTH),
            UserNameValidator(),
        ],
        null=False,
        blank=False
    )

    email = models.EmailField(
        null=False,
        blank=False
    )
    age = models.PositiveIntegerField(
        null=True,
        blank=True
    )


