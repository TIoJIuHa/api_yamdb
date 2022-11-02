from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        verbose_name="Имя пользователя",
        max_length=150,
        unique=True,
    )
    email = models.EmailField(
        ("Электронная почта"),
        unique=True,
    )
    confirmation_code = models.CharField(
        max_length=100,
        blank=True,
    )
    first_name = models.CharField(
        verbose_name="Имя",
        max_length=150,
        blank=True,
    )
    last_name = models.CharField(
        verbose_name="Фамилия",
        max_length=150,
        blank=True,
    )
    bio = models.TextField(
        verbose_name="Биография",
        blank=True,
    )

    ROLE_CHOICES = [
        ("user", "user"),
        ("moderator", "moderator"),
        ("moderator", "admin"),
    ]

    role = models.CharField(
        verbose_name="Пользовательская роль",
        max_length=9,
        choices=ROLE_CHOICES,
        default="user",
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self) -> str:
        return self.username
