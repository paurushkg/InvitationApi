from rest_framework import serializers
from accounts.models import User


class UserRegisterSerializer(serializers.ModelSerialzer):

    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def save(self):
        user = User(
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            phone_number=self.validated_data['phone_number'],
        )
        if self.validated_data['password'] != self.validated_data['confirm_password']:
            raise serializers.ValidationError({'detail': "password don't match"})

