from django.db import models


class Category(models.Model):
    '''Таблица категорий (типы) произведений'''
    name = models.CharField()
    slug = models.SlugField(
        unique=True
    )


class Genre(models.Model):
    '''Таблица с категориями жанров'''
    name = models.CharField()
    slug = models.SlugField(
        unique=True
    )


class Titles(models.Model):
    '''Основная таблица произведений, к которым пишут отзывы'''
    '''(определённый фильм, книга или песенка).'''
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE
    )
    name = models.CharField()
    year = models.DateField(
        'Дата выхода',
    )
    description = models.TextField(
        max_length=256
    )
