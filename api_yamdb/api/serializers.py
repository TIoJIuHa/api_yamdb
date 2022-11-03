from rest_framework import serializers

from reviews.models import Titles, Category, Genre


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id',
                  'name',
                  'slug')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id',
                  'name',
                  'slug')


class TitlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Titles
        fields = ('id',
                  'name',
                  'category',
                  'genre',
                  'description',
                  'year')