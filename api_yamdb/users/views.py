from api.permissions import IsAdmin
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import filters, status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import User

from .serializers import (
    RegistrationSerializer,
    UserSerializer,
    VerificationSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "username"
    permission_classes = [IsAdmin]
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ["username"]

    @action(
        detail=True,
        methods=["GET", "PATCH"],
        permission_classes=[IsAuthenticated],
    )
    def me(self, request):
        if request.method == "PATCH":
            serializer = self.get_serializer(
                request.user, data=request.data, partial=True
            )
            if not (serializer.is_valid()):
                return Response(
                    serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )
            if serializer.validated_data.get("role"):
                if request.user.role != "admin" or not (
                    request.user.is_superuser
                ):
                    serializer.validated_data["role"] = request.user.role
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        serializer = self.get_serializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([AllowAny])
def registration_view(request):
    serializer = RegistrationSerializer(data=request.data)
    if not (serializer.is_valid()):
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    username = request.data.get("username")
    email = request.data.get("email")
    user, created = User.objects.get_or_create(username=username, email=email)
    confirmation_code = Token.objects.create(user=user)
    send_mail(
        "YaMDb: код для подтверждения регистрации",
        f"Ваш код для получения токена: {confirmation_code}",
        "from@yamdb.com",
        [email],
        fail_silently=False,
    )
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([AllowAny])
def verification_view(request):
    serializer = VerificationSerializer(data=request.data)
    if not (serializer.is_valid()):
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    username = request.data.get("username")
    confirmation_code = request.data.get("confirmation_code")
    check_username = get_object_or_404(User, username=username)
    check_user_code = get_object_or_404(User, auth_token=confirmation_code)
    if check_username != check_user_code:
        return Response(
            data={"Error": "Неверный код подтверждения"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    token = RefreshToken.for_user(check_username)
    return Response(
        data={"token": str(token.access_token)}, status=status.HTTP_200_OK
    )
