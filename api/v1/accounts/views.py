from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth.models import User

from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import SignupSerializer


class SignupView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User created successfully"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            if not refresh_token:
                return Response(
                    {"error": "Refresh token is required"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {"message": "Logout successful"},
                status=status.HTTP_205_RESET_CONTENT
            )
        except Exception as e:
            return Response(
                {"error": "Invalid refresh token"},
                status=status.HTTP_400_BAD_REQUEST
            )

from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

class CreateAdminView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        if User.objects.filter(username="admin").exists():
            return Response({"message": "Admin already exists"})

        User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="admin@123"
        )
        return Response({"message": "Admin user created"})
