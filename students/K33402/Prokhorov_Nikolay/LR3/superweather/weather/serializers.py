from rest_framework import serializers
from .models import *


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class ForecastSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = WeatherForecast
        fields = '__all__'


class CityDailySerializer(serializers.ModelSerializer):

    class Meta:
        model = WeatherDaily
        fields = '__all__'
