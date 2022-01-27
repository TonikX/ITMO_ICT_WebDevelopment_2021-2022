from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from hotel.models import *
from hotel.serializers import RoomSerializer, StaffSerializer, GuestSerializer, CleaningSerializer


class RoomAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class StaffAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()


class GuestAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = GuestSerializer
    queryset = Guest.objects.all()


class CleaningAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CleaningSerializer
    queryset = Cleaning.objects.all()