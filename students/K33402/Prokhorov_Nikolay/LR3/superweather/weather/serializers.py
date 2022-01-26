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


class CityDailySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherDaily
        fields = '__all__'


class ForecastSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    current = WeatherCurrentSerializer()
    daily = CityDailySerializer(many=True)

    class Meta:
        model = WeatherForecast
        fields = '__all__'


class FavoriteCityEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteCity
        fields = ('city',)


class FavoriteCitySerializer(serializers.ModelSerializer):
    city_info = CitySerializer(read_only=True, source='city')
    city_weather = ForecastSerializer(read_only=True, source='city_set', many=True)

    class Meta:
        model = FavoriteCity
        fields = ('city', 'city_info', 'city_weather')
