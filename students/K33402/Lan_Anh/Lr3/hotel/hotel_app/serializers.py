from rest_framework import serializers
from .models import *

class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'sex', 'nationality', 'passport_no']

class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'sex', 'license', 'workExp']

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"

class RoomSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer()
    class Meta:
        model = Room
        fields = "__all__"

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = "__all__"

# Functional analytics views

class BookingBillSerializer(serializers.ModelSerializer):
    bills = BillSerializer(many=True)
    main_guest = VisitorSerializer()
    room = RoomSerializer()

    class Meta:
        model = Booking
        fields = "__all__"

class BookingOfVisitorSerializer(serializers.ModelSerializer):
    room = RoomSerializer()

    class Meta:
        model = Booking
        fields = ['id', 'booking_code', 'date_checkin', 'date_checkout', 'room']

class HotelInfoSerializer(serializers.ModelSerializer):
    owner = HostSerializer()
    class Meta:
        model = Hotel
        fields = "__all__"