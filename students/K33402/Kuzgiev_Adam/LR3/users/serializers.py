from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers


# Для пользователя выводим его имя пользователя и список выборанных городов
class MyUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ['username', 'cities']

    cities = serializers.SlugRelatedField('city_id', many=True, read_only=True)


# При регистрации нужны только имя пользователя и пароль
class MyUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['username', 'password']
