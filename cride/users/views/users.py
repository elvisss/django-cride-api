"""User views"""
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from cride.users.serializers import UserModelSerializer, UserLoginSerializer, UserSignUpSerializer, AccountVerificationSerializer

class UserLoginAPIView(APIView):
    """User Login API View"""

    def post(self, request, *args, **kwargs):
        """Handle HTPP POST request."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        serializer = UserModelSerializer(user)
        data = {
            'user': serializer.data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)

class UserSignUpAPIView(APIView):
    """User signup API View"""

    def post(self, request, *args, **kwargs):
        """Handle HTPP POST request."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)

class AccountVerificationAPIView(APIView):
    """User verify account API View"""

    def get(self, request, *args, **kwargs):
        """Handle HTTP GET requiest"""
        serializer = AccountVerificationSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {
            'message': 'Congratulation, your account has been verified'
        }
        return Response(data, status=status.HTTP_200_OK)
