from rest_framework import generics, permissions

from tickets.models import Flight, FlightBooking
from tickets.serializers import (CreateFlightBookingSerializer,
                                 FlightBookingSerializer, FlightSerializer)


class FlightListView(generics.ListAPIView):
    queryset = Flight.objects.all()
    filterset_fields = ('company', 'departure_airport', 'arrival_airport',
                        'departure_datetime', 'arrival_datetime', 'price')
    serializer_class = FlightSerializer


class FlightDetailView(generics.RetrieveAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class CreateBookingView(generics.CreateAPIView):
    queryset = FlightBooking.objects.all()
    serializer_class = CreateFlightBookingSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MyBookingsView(generics.ListAPIView):
    serializer_class = FlightBookingSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = FlightBooking.objects.none()

    def get_queryset(self):
        return FlightBooking.objects.filter(user=self.request.user)
