from rest_framework import serializers
from .models import Room, Groups


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = '__all__'
