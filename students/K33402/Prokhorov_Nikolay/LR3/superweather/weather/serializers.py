from rest_framework import serializers
from .models import *


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class WeatherCurrentSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherCurrent
        fields = '__all__'


class ForecastSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    current = WeatherCurrentSerializer()

    class Meta:
        model = WeatherForecast
        fields = '__all__'


class CityDailySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherDaily
        fields = '__all__'
