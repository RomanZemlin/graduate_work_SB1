from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers

User = get_user_model()


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    password = serializers.CharField(required=True)

    class Meta:
        model = User
        exclude = ('id',)


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('id', 'password')
