from rest_framework import viewsets

from reviews.models import Titles, Genre, Category
from .serializers import TitlesSerializer, GenreSerializer, CategorySerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    '''Вьюсет для модели Категории. Читать может любой пользователь'''
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    '''Вьюсет для модели Жанры. Читать может любой пользователь'''
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class TitlesViewSet(viewsets.ReadOnlyModelViewSet):
    '''Вьюсет для Произведений. Читать может любой пользователь'''
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer
