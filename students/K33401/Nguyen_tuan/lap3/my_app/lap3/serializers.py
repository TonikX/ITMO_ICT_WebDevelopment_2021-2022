from rest_framework import serializers
from .models import *


#Guest
class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = "__all__"


class CreateGuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = "__all__"


#Staff
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"


class CreateStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"


#Type
class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"


class CreateTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"


#Status
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"


class CreateStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"


#Floor
class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = "__all__"


class CreateFloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = "__all__"


#Room
class RoomSerializer(serializers.ModelSerializer):
    type_id = TypeSerializer()
    status_id = StatusSerializer()
    floor_id = FloorSerializer()

    class Meta:
        model = Room
        fields = "__all__"


class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


#Bill
class BillSerializer(serializers.ModelSerializer):
    room_id = RoomSerializer()
    guest_id = GuestSerializer()
    class Meta:
        model = Bill
        fields = "__all__"


class CreateBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = "__all__"


#Schedule
class ScheduleSerializer(serializers.ModelSerializer):
    staff_id = StaffSerializer()
    floor_id = FloorSerializer()
    class Meta:
        model = Schedule
        fields = "__all__"


class CreateScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"