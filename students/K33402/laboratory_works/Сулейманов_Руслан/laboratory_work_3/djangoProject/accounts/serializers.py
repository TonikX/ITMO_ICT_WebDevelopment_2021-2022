from rest_framework import serializers

from accounts.models import User, Membership
from city_app.models import CityList


class CitySerialzer(serializers.ModelSerializer):
    class Meta:
        model = CityList
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    cities = CitySerialzer(many=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "birthday",
            "cities"
        ]


class CityUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ["id", "city", "user", "date_joined"]
        read_only_fields = ["user", "date_joined"]
