from rest_framework import serializers
from .models import *


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"
        depth = 1


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class BillViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['client']
        depth = 1


class ClientCountSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ['city', 'count']

    def get_count(self, obj):
        return obj["count"]


class EmployeeS(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['date', 'employee']
        depth = 1


class AvailableRoomSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source="get_type_display", read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'type', 'number', 'price', 'floor']


class RoomCountSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = ['floor', 'count']

    def get_count(self, obj):
        return obj["count"]



