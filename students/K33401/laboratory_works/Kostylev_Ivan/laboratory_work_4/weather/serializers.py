from rest_framework import serializers

from weather.models import User, Town, Country


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Town
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
