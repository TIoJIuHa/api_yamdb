from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from reviews.models import Category, Genre, Review, Title
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend

from .permissions import IsAdminOrReadOnly, IsAuthorModeratorAdminOrReadOnly
from .serializers import (
    CategorySerializer,
    CommentSerializer,
    GenreSerializer,
    ReviewSerializer,
    TitleSerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Категории. Делать запрос может любой пользователь,"""

    """редактировать и удалять - только админ"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [
        IsAdminOrReadOnly,
    ]
    pagination_class = LimitOffsetPagination

    # def get_permissions(self):
    #     if self.action == "retrieve":
    #         return (permissions.IsAuthenticatedOrReadOnly,)
    #     return super().get_permissions()


class GenreViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Жанры. Делать запрос может любой пользователь,"""

    """редактировать и удалять - только админ"""
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [
        IsAdminOrReadOnly,
    ]
    pagination_class = LimitOffsetPagination

    # def get_permissions(self):
    #     if self.action == "retrieve":
    #         return (permissions.IsAuthenticatedOrReadOnly,)
    #     return super().get_permissions()


class TitleViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Произведения. Делать запрос может любой,"""

    """редактировать и удалять - только админ"""
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = [
        IsAdminOrReadOnly,
    ]
    pagination_class = LimitOffsetPagination

    # def get_permissions(self):
    #     if self.action == "retrieve":
    #         return (permissions.IsAuthenticatedOrReadOnly,)
    #     return super().get_permissions()


class ReviewViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели отзыва"""

    serializer_class = ReviewSerializer
    permission_classes = [IsAuthorModeratorAdminOrReadOnly]
    pagination_class = LimitOffsetPagination
    
    def perform_create(self, serializer):
        title = get_object_or_404(Title, id=self.kwargs.get("title_id"))
        serializer.save(user=self.request.user, title=title)

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs.get("title_id"))
        return title.reviews.all()


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели комментария"""

    serializer_class = CommentSerializer
    permission_classes = [IsAuthorModeratorAdminOrReadOnly]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        review = get_object_or_404(
            Review,
            id=self.kwargs.get("review_id"),
            title=self.kwargs.get("title_id")
        )
        serializer.save(user=self.request.user, review=review)

    def get_queryset(self):
        review = get_object_or_404(Review, id=self.kwargs.get("review_id"))
        return review.comments.all()
