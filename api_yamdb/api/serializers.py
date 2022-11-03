from rest_framework import serializers
from reviews.models import Category, Comment, Genre, Review, Titles


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "slug")


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name", "slug")


class TitlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Titles
        fields = ("id", "name", "category", "genre", "description", "year")


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Review
        read_field_only = ("title",)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field="username"
    )

    class Meta:
        fields = (
            "id",
            "author",
            "review",
            "text",
            "created",
        )
        model = Comment
        read_only_fields = ("review",)
