from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from reviews.models import Category, Genre, Review, Titles

from .permissions import IsAuthorOrReadOnly
from .serializers import (
    CategorySerializer,
    CommentSerializer,
    GenreSerializer,
    ReviewSerializer,
    TitlesSerializer,
)


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


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly

    def perform_create(self, serializer):
        title_id = self.kwargs.get("title_id")
        title = get_object_or_404(Title, id=title_id)
        serializer.save(user=self.request.user, title=title)

    def get_queryset(self):
        title_id = self.kwargs.get("title_id")
        title = get_object_or_404(Title, id=title_id)
        return title.reviews


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly

    def perform_create(self, serializer):
        review_id = self.kwargs.get("review_id")
        review = get_object_or_404(Review, id=review_id)
        serializer.save(user=self.request.user, review=review)

    def get_queryset(self):
        review_id = self.kwargs.get("review_id")
        review = get_object_or_404(Review, id=review_id)
        return review.comments
