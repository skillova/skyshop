from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field import modelfields


class User(AbstractUser):
    username = None

    avatar = models.ImageField(
        upload_to="users/avatars/",
        null=True,
        blank=True,
        verbose_name="Avatar"
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Email"
    )
    phone = modelfields.PhoneNumberField(
        unique=True,
        null=True,
        blank=True,
        verbose_name="Phone number"
    )
    country = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name="Phone number"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
