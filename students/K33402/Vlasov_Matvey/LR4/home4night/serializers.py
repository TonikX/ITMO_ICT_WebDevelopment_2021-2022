from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import *


class UserDefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name"]


class UserCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "password"]
        extra_kwargs = {'first_name': {'required': True, 'allow_blank': False},
                        'last_name': {'required': True, 'allow_blank': False}}

    def create(self, validated_data):
        if 'pbkdf2_sha256' not in validated_data['password']:
            validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserCreateUpdateSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        if 'pbkdf2_sha256' not in validated_data['password']:
            validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserCreateUpdateSerializer, self).update(instance, validated_data)


class LandlordSerializer(serializers.ModelSerializer):
    user = UserDefaultSerializer()

    class Meta:
        model = Landlord
        fields = "__all__"


class LandlordCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landlord
        fields = "__all__"


class TenantSerializer(serializers.ModelSerializer):
    user = UserDefaultSerializer()

    class Meta:
        model = Tenant
        fields = "__all__"


class TenantCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = "__all__"


class PropertySerializer(serializers.ModelSerializer):
    owner = LandlordSerializer()

    class Meta:
        model = Property
        fields = "__all__"


class PropertyCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    tenant = TenantSerializer()
    property = PropertySerializer()

    class Meta:
        model = Booking
        fields = ["tenant", "property", "checkin", "checkout", "total_price", "status"]


class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["tenant", "property", "checkin", "checkout", "status"]

    def create(self, validated_data):
        nights = (validated_data["checkout"] - validated_data["checkin"]).days
        price = Property.objects.get(id=validated_data["property"].id).price
        validated_data["total_price"] = nights * price
        return super(BookingCreateSerializer, self).create(validated_data)


class BookingUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["tenant", "property", "checkin", "checkout", "total_price", "status"]


class ReviewSerializer(serializers.ModelSerializer):
    booking = BookingSerializer()

    class Meta:
        model = Review
        fields = "__all__"


class ReviewCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
