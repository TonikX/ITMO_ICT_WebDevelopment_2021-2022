from .serializers import *
from rest_framework import generics
from django.db.models import Count
from .models import *

# Create your views here.


class BillView(generics.ListAPIView):
    serializer_class = BillSerializer
    queryset = Bill.objects.all()


class BillCreateAPIView(generics.CreateAPIView):
    serializer_class = BillSerializer
    queryset = Bill.objects.all()


class BillDestroy(generics.RetrieveDestroyAPIView):
    serializer_class = BillSerializer
    queryset = Bill.objects.all()


class BillUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = BillSerializer
    queryset = Bill.objects.all()

# ----------------------------


class ClientView(generics.ListAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class ClientCreateAPIView(generics.CreateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class ClientUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class ClientDestroy(generics.RetrieveDestroyAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

# ----------------------------


class ScheduleView(generics.ListAPIView):
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()


class ScheduleCreateAPIView(generics.CreateAPIView):
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()


class ScheduleDestroy(generics.RetrieveDestroyAPIView):
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()


class ScheduleUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()

# ----------------------------


class RoomView(generics.ListAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class RoomCreateAPIView(generics.CreateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class RoomUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class RoomDestroy(generics.RetrieveDestroyAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


# ----------------------------


class EmployeeView(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeCreate(generics.CreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeDestroy(generics.RetrieveDestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()



# ----------------------------
class BillAPIView(generics.ListAPIView):
    serializer_class = BillViewSerializer

    def get_queryset(self):
        queryset = Bill.objects.all()
        checkin = self.request.query_params.get('checkin')
        checkout = self.request.query_params.get('checkout')
        number = self.request.query_params.get('number')
        if checkin and checkout and number is not None:
            queryset = Bill.objects.all().filter(date_checkin__gte=checkin,
                                                 date_checkout__lte=checkout,
                                                 room__number=number)
        return queryset


class ClientCount(generics.ListAPIView):
    serializer_class = ClientCountSerializer

    def get_queryset(self):
        city = self.request.query_params.get('city')
        c = Client.objects.annotate(num_clients=Count('id')).filter(city=city).count()
        queryset = [{'city': city, 'count': c}]
        return queryset


class EmployeeAPIView(generics.ListAPIView):
    serializer_class = EmployeeS

    def get_queryset(self):
        client = self.request.query_params.get('client')
        num_room = Room.objects.get(client__last_name=client)
        date = self.request.query_params.get('date')
        queryset = Schedule.objects.all().filter(date=date, room__number=num_room.number)
        return queryset


class AvailableRoomAPIView(generics.ListAPIView):
    serializer_class = AvailableRoomSerializer

    def get_queryset(self):
        return Room.objects.all().filter(state="+")


class RoomCount(generics.ListAPIView):
    serializer_class = RoomCountSerializer

    def get_queryset(self):
        floor = self.request.query_params.get('floor')
        c = Room.objects.annotate(num_rooms=Count('id')).filter(floor=floor).count()
        return [{'floor': floor, 'count': c}]

