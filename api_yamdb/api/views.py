from rest_framework import permissions, viewsets
from reviews.models import Category, Genre, Titles

from .serializers import CategorySerializer, GenreSerializer, TitlesSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Категории. Делать запрос может любой пользователь,"""

    """редактировать и удалять - только админ"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [
        permissions.IsAdminUser,
    ]

    def get_permissions(self):
        if self.action == "retrieve":
            return (permissions.IsAuthenticatedOrReadOnly,)
        return super().get_permissions()


class GenreViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Жанры. Делать запрос может любой пользователь,"""

    """редактировать и удалять - только админ"""
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [
        permissions.IsAdminUser,
    ]

    def get_permissions(self):
        if self.action == "retrieve":
            return (permissions.IsAuthenticatedOrReadOnly,)
        return super().get_permissions()


class TitlesViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Произведения. Делать запрос может любой,"""

    """редактировать и удалять - только админ"""
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer
    permission_classes = [
        permissions.IsAdminUser,
    ]

    def get_permissions(self):
        if self.action == "retrieve":
            return (permissions.IsAuthenticatedOrReadOnly,)
        return super().get_permissions()
