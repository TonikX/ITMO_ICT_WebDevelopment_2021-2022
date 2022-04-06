from rest_framework import serializers

from weather.models import User, Town


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Town
        fields = '__all__'
