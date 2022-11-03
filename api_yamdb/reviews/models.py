from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from users.models import User


class Category(models.Model):
    """Таблица категорий (типы) произведений"""

    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)


class Genre(models.Model):
    """Таблица с категориями жанров"""

    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)


class Title(models.Model):
    """Основная таблица произведений, к которым пишут отзывы"""

    """(определённый фильм, книга или песенка)."""
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    year = models.DateField(
        "Дата выхода",
    )
    description = models.TextField(max_length=256)


class Review(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviews"
    )
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name="reviews"
    )
    text = models.TextField("Текст отзыва")
    score = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"{self.text} and {self.rating}"


class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name="comments"
    )
    text = models.TextField("Текст комментария")

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.text
