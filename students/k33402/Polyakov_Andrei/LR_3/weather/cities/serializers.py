from rest_framework import serializers
from cities.models import City, CityPreference


class CitySeriazlier(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class CityPreferenceReadSeriazlier(serializers.ModelSerializer):
    city = CitySeriazlier()

    class Meta:
        model = CityPreference
        fields = ['id', 'city']


class CityPreferenceWriteSeriazlier(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CityPreference
        fields = ['id', 'user', 'city']