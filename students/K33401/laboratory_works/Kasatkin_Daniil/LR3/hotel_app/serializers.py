from rest_framework import serializers, fields
from .models import *
from hotel_app.models import Place
from django.contrib.postgres.fields import ArrayField


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CreateHostUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['is_host']


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number', 'email', 'first_name', 'password', 'is_active']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class PlaceSerializer(serializers.ModelSerializer):
    host = UserSerializer()
    place_type = serializers.CharField(source='get_place_type_display')
    place_offers = serializers.CharField(source='get_place_offers_display')

    class Meta:
        model = Place
        fields = '__all__'


class CreatePlaceSerializer(serializers.ModelSerializer):
    place_offers = serializers.ListField()

    class Meta:
        model = Place
        fields = '__all__'


class ReserveSerializer(serializers.ModelSerializer):
    guest = UserSerializer()
    place = PlaceSerializer()

    class Meta:
        model = Reserve
        fields = '__all__'


class CreateReserveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserve
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    place = PlaceSerializer()

    class Meta:
        model = Review
        fields = '__all__'


class CreateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
