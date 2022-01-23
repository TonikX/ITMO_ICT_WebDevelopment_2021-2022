from rest_framework import serializers
from cities.models import City, FavouriteCity


class CitySerializer(serializers.ModelSerializer):
    """Serializer for cities"""

    class Meta:
        model = City
        fields = '__all__'


class FavouriteCitySerializer(serializers.ModelSerializer):
    """Serializer for favourite cities"""

    class Meta:
        model = FavouriteCity
        fields = ['id', 'user', 'city', 'city_id']

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    city = CitySerializer(many=True, read_only=True)
    city_id = serializers.PrimaryKeyRelatedField(queryset=City.objects.all(), write_only=True, source='city')


class LatLonSerializer(serializers.Serializer):
    """Serializer for latitude and longtitude"""
    lat = serializers.FloatField()
    lon = serializers.FloatField()
