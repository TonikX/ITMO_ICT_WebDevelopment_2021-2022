from django.shortcuts import render
from rest_framework import generics
from flights.serializers import *


class PassengerListView(generics.ListAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class PassengerCreateView(generics.CreateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class PassengerEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class PlaneListView(generics.ListAPIView):
    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer


class PlaneCreateView(generics.CreateAPIView):
    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer


class PlaneEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer


class FlightListView(generics.ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class FlightCreateView(generics.CreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class FlightEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class TicketListView(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketCreateView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class AirCompanyListView(generics.ListAPIView):
    queryset = AirCompany.objects.all()
    serializer_class = AirCompanySerializer


class AirCompanyCreateView(generics.CreateAPIView):
    queryset = AirCompany.objects.all()
    serializer_class = AirCompanySerializer


class AirCompanyEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AirCompany.objects.all()
    serializer_class = AirCompanySerializer
