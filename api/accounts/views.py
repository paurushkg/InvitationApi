from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from .serializers import UserRegisterSerializer, ChangePasswordSerializer


class UserRegisterView(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['detail'] = 'user registered'
            data['phone number'] = user.phone_number
        else:
            data = serializer.errors
            return Response(data)
        return Response(data, status=status.HTTP_201_CREATED)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = AccessToken(refresh_token)
            token.blacklist()
            return Response({'detail': 'Successfully Logout'}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({'detail': 'Not Logout '}, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(APIView):

    def post(self, request):
        phone_number = request.user.phone_number

        serializer = ChangePasswordSerializer(request.data)
        data = {}
        if serializer.is_valid():
            serializer.save(phone_number)
            data['detail'] = 'password changed successfully'
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
