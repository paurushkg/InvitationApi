from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


from . serializers import UserRegisterSerializer


class UserRegisterView(APIView):

    def post(self, request, *args, **kwargs):
        print(request.user)
        if request.user.is_authenticated:
            return Response({'detail': 'You are already registered and authenticated'}, status=400)
        serializer = UserRegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['detail'] = 'user registered'
            data['phone number'] = user.phone_number
        else:
            data = serializer.errors
            return Response(data)
        return Response(data, status=201)
