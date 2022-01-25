from .models import *
from rest_framework import serializers


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CityModel
        fields = '__all__'


class WeatherSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = WeatherModel
        fields = '__all__'


class MyCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCitiesModel
        fields = '__all__'


class MyCityFullSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    weather = WeatherSerializer()

    class Meta:
        model = WeatherModel
        fields = '__all__'
