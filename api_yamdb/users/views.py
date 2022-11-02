from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from users.models import User

from .serializers import RegistrationSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "username"

    @action(detail=True, methods=["GET", "PATCH"])
    def me(self, request):
        if request.method == "PATCH":
            serializer = self.get_serializer(request.user, data=request.data)
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


@action(detail=True, methods=["POST"], url_path="signup")
def registration_view(request):
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid:
        send_mail(
            "Subject here",
            "Here is the message.",
            "from@yamdb.com",
            ["to@example.com"],
            fail_silently=False,
        )
