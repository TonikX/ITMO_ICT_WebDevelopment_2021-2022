from rest_framework import serializers
from .models import *


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class FavoriteCitySerializer(serializers.ModelSerializer):
    city_info = CitySerializer(read_only=True, source='city')

    class Meta:
        model = FavoriteCity
        fields = ('city', 'city_info')


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
