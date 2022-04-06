from rest_framework import serializers
from .models import *


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = "__all__"


class FavouriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favourite
        fields = "__all__"


class CityCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)

    def create(self, validated_data):
        city = City(**validated_data)
        city.save()
        return City(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    favourite_cities = serializers.SlugRelatedField(read_only=True, many=True, slug_field='name')

    class Meta:
        model = User
        fields = "__all__"


class FavouriteCreateSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    city_id = serializers.IntegerField()

    def create(self, validated_data):
        favourite = Favourite(**validated_data)
        favourite.save()
        return Favourite(**validated_data)
