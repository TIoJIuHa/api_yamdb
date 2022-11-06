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
    genre = GenreSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Title
        fields = ("id", "name", "category", "genre", "year")


class TitlePostSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = Title
        fields = ("id", "name", "category", "genre", "year")

    def create(self, validated_data):
        genre = validated_data.pop('genre')
        title = Title.objects.create(**validated_data)

        for genries in genre:
            genre_current = Genre.objects.get(**genries)
            GenreTitle.objects.create(genries=genre_current, title=title)
        return title


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
