"""User views"""
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework import status, viewsets
from rest_framework.response import Response
from cride.users.serializers import UserModelSerializer, UserLoginSerializer, UserSignUpSerializer, AccountVerificationSerializer
from rest_framework.decorators import action

class UserViewSet(viewsets.GenericViewSet):
    """User View set.

    Handle sign up, login and account verification.
    """

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """User sign up."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def login(self, request):
        """User login."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'])
    def verify(self, request):
        """Account verification."""
        serializer = AccountVerificationSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {
            'message': 'Congratulation, your account has been verified'
        }
        return Response(data, status=status.HTTP_200_OK)

""" class UserLoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
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
    def post(self, request, *args, **kwargs):
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)

class AccountVerificationAPIView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = AccountVerificationSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {
            'message': 'Congratulation, your account has been verified'
        }
        return Response(data, status=status.HTTP_200_OK)
 """
