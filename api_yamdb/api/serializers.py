import datetime as dt

from django.shortcuts import get_list_or_404
from rest_framework import serializers
from reviews.models import Category, Comment, Genre, GenreTitle, Review, Title


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


class TitleSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(), slug_field="slug", many=True
    )
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field="slug"
    )

    class Meta:
        model = Title
        fields = (
            "id",
            "name",
            "category",
            "genre",
            "year",
            "description",
        )

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["category"] = CategorySerializer(instance.category).data
        response["genre"] = GenreSerializer(instance.genre, many=True).data
        return response

    def create(self, validated_data):
        genre_slug = validated_data.pop("genre")
        title = Title.objects.create(**validated_data)

        for genries in genre_slug:
            genre_current = Genre.objects.get(slug=genries.slug)
            GenreTitle.objects.create(genre=genre_current, title=title)
        return title

    def validate_date(self, value):
        year = dt.date.today().year
        if value > year:
            raise serializers.ValidationError(
                "Год не может быть больше текущего"
            )
        return value

    def get_rating(self, obj):
        review_list = get_list_or_404(Review, title=obj)
        sum = 0
        for review in review_list:
            sum += review.score
        return round(sum / len(review_list))

    # def get_rating(self, obj):
    #    review_object = Review.objects.filter(
    #                                          title=obj.id).aggregate(Avg('score'))
    #    avg_score = review_object['score__avg']
    #    if avg_score is None:
    #        return 0
    #    return float('{:.1f}').format(avg_score)


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username", read_only=True
    )
    score = serializers.IntegerField(min_value=1, max_value=10)

    class Meta:
        model = Review
        fields = "__all__"
        read_only_fields = ("title",)

    def validate(self, data):
        if self.context["request"].method == "POST":
            if Review.objects.filter(
                author=self.context["request"].user,
                title=self.context["view"].kwargs.get("title_id"),
            ).exists():
                raise serializers.ValidationError(
                    "Нельзя оставить отзыв на одно произведение дважды"
                )
        return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field="username"
    )

    class Meta:
        fields = "__all__"
        model = Comment
        read_only_fields = ("review",)
