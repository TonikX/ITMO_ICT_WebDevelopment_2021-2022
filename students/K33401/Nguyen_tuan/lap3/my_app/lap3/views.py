from django.db.models import query
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics


# guest
class GuestListView(generics.ListAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


class GuestRetrieveView(generics.RetrieveDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


class GuestUpdateView(generics.UpdateAPIView):
    queryset = Guest.objects.all()
    serializer_class = CreateGuestSerializer


class GuestCreateView(generics.CreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = CreateGuestSerializer


# staff
class StaffListView(generics.ListAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class StaffRetrieveView(generics.RetrieveDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class StaffUpdateView(generics.UpdateAPIView):
    queryset = Staff.objects.all()
    serializer_class = CreateStaffSerializer


class StaffCreateView(generics.CreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = CreateStaffSerializer


# floor
class FloorListView(generics.ListAPIView):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer


class FloorRetrieveView(generics.RetrieveDestroyAPIView):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer


class FloorUpdateView(generics.UpdateAPIView):
    queryset = Floor.objects.all()
    serializer_class = CreateFloorSerializer


class FloorCreateView(generics.CreateAPIView):
    queryset = Floor.objects.all()
    serializer_class = CreateFloorSerializer


# status
class StatusListView(generics.ListAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class StatusRetrieveView(generics.RetrieveDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class StatusUpdateView(generics.UpdateAPIView):
    queryset = Status.objects.all()
    serializer_class = CreateStatusSerializer


class StatusCreateView(generics.CreateAPIView):
    queryset = Status.objects.all()
    serializer_class = CreateStatusSerializer


# type
class TypeListView(generics.ListAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class TypeRetrieveView(generics.RetrieveDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class TypeUpdateView(generics.UpdateAPIView):
    queryset = Type.objects.all()
    serializer_class = CreateTypeSerializer


class TypeCreateView(generics.CreateAPIView):
    queryset = Type.objects.all()
    serializer_class = CreateTypeSerializer


# room
class RoomListView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomRetrieveView(generics.RetrieveDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomUpdateView(generics.UpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = CreateRoomSerializer


class RoomCreateView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = CreateRoomSerializer


# Bill
class BillListView(generics.ListAPIView):
    # queryset = Bill.objects.all()
    serializer_class = BillSerializer

    def get_queryset(self):
        queryset = Bill.objects.all()
        params = self.request.query_params

        room_id = params.get('room', None)
        check_in = params.get('check_in', None)
        check_out = params.get('check_out', None)

        if room_id:
            queryset = queryset.filter(room_id__number=room_id)

        if check_in:
            queryset = queryset.filter(check_in__lte=check_in)

        if check_out:
            queryset = queryset.filter(check_out__gte=check_out)

        return queryset


class BillRetrieveView(generics.RetrieveDestroyAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer


class BillUpdateView(generics.UpdateAPIView):
    queryset = Bill.objects.all()
    serializer_class = CreateBillSerializer


class BillCreateView(generics.CreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = CreateBillSerializer


# schedule
class ScheduleListView(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class ScheduleRetrieveView(generics.RetrieveDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class ScheduleUpdateView(generics.UpdateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = CreateScheduleSerializer


class ScheduleCreateView(generics.CreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = CreateScheduleSerializer