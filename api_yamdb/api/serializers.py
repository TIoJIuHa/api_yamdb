import datetime as dt

from rest_framework import serializers
from reviews.models import (Category,
                            Comment,
                            Genre,
                            Review,
                            Title,
                            GenreTitle)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", "slug")
        lookup_field = "slug"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("name", "slug")
        lookup_field = "slug"


class TitleGetSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(read_only=True,
                                         slug_field="slug",
                                         many=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Title
        fields = ("id", "name", "category", "genre", "year", "description")


class TitlePostSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(queryset=Genre.objects.all(),
                                         slug_field="slug",
                                         many=True)
    category = serializers.SlugRelatedField(queryset=Category.objects.all(),
                                            slug_field="slug")

    class Meta:
        model = Title
        fields = ("id", "name", "category", "genre", "year", "description")

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["category"] = CategorySerializer(instance.category).data
        response["genre"] = GenreSerializer(instance.genre, many=True).data
        return response

    def create(self, validated_data):
        genre_slug = validated_data.pop('genre')
        title = Title.objects.create(**validated_data)

        for genries in genre_slug:
            genre_current = Genre.objects.get(slug=genries.slug)
            GenreTitle.objects.create(genre=genre_current, title=title)
        return title
    
    def validate_date(self, value):
        year = dt.date.today().year
        if value > year:
            raise serializers.ValidationError(
                'Год не может быть больше текущего')
        return value


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "user",
            "title",
            "text",
            "score",
        )
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
