from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenViewBase

from drf_spectacular.utils import extend_schema, extend_schema_view, inline_serializer

from account.serializers import (
    CustomUserSerializer,
    TokenBlacklistSerializer,
)
from account.extended_schema import logout_schema


# Create your views here.
class CustomUserCreateAPIView(generics.CreateAPIView):
    """
    Creates New User
    """
    permission_classes = [AllowAny]
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(
                    data=serializer.data,
                    status=status.HTTP_201_CREATED
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


@extend_schema_view(post=extend_schema(responses={**logout_schema}))
class LogoutAPIView(TokenViewBase):
    """
    Logout User
    """
    serializer_class = TokenBlacklistSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            data={'message': 'Logged out Successfully'},
            status=status.HTTP_204_NO_CONTENT
        )
