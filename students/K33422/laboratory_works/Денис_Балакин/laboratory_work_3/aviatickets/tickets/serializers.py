from rest_framework import serializers

from tickets.models import Airport, Company, Flight, FlightBooking


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class FlightSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    departure_airport = AirportSerializer()
    arrival_airport = AirportSerializer()

    class Meta:
        model = Flight
        fields = (
            'id',
            'company',
            'departure_airport',
            'arrival_airport',
            'departure_datetime',
            'arrival_datetime',
            'price',
            'flight_length'
        )


class FlightBookingSerializer(serializers.ModelSerializer):
    flight = FlightSerializer()

    class Meta:
        model = FlightBooking
        fields = ('id', 'flight')


class CreateFlightBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightBooking
        fields = ('id', 'flight')
