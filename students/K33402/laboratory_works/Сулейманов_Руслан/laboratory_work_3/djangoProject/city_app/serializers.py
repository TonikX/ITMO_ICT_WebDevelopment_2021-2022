from rest_framework import serializers
from city_app.models import CityList


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CityList
        fields = "__all__"
