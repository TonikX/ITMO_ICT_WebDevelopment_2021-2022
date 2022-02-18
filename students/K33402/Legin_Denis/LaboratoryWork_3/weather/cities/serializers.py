from rest_framework import serializers
from cities.models import City, CityPreference


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class CityPreferenceReadSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = CityPreference
        fields = ['id', 'city']


class CityPreferenceWriteSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CityPreference
        fields = ['id', 'user', 'city']