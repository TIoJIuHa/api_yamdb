from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "bio",
            "role",
        )


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")

    def validate_username(self, username):
        if username.lower() == "me":
            raise serializers.ValidationError(
                'Использовать имя "me" запрещено!'
            )
        return username


class TokenSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ("username", "confirmation_code")
