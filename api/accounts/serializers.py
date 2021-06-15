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


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    new_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    confirm_new_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    def save(self, phone_number):
        old_password = self.validated_data['old_password']
        new_password = self.validated_data['new_password']
        confirm_new_password = self.validated_data['confirm_new_password']

        if new_password != confirm_new_password:
            raise serializers.ValidationError({'detail': "password don't match"})

        user = User.objects.get(phone_number=phone_number)
        if not user.check_password(old_password):
            raise serializers.ValidationError({'detail': "wrong password"})
        else:
            user.set_password(new_password)
            user.save()
            return user
