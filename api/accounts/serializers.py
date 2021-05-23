from rest_framework import serializers
from . models import User


class UserRegisterSerializer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        password = self.validated_data['password']
        if password != self.validated_data['confirm_password']:
            raise serializers.ValidationError({'detail': "password don't match"})

        user = User(
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            phone_number=self.validated_data['phone_number'],
        )
        user.set_password(password)
        user.save()
        return user



