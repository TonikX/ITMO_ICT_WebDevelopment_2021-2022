from datetime import timedelta
from django.utils.dateparse import parse_date
from rest_framework import generics

from .models import *
from .serializers import *


class UserRetrieveView(generics.RetrieveAPIView):
    """ Get information about specific user """

    queryset = User.objects.all()
    serializer_class = UserDefaultSerializer


class UserListView(generics.ListAPIView):
    """ Get user list """
    queryset = User.objects.all()
    serializer_class = UserDefaultSerializer


class UserCreateView(generics.CreateAPIView):
    """ Create user """
    queryset = User.objects.all()
    serializer_class = UserCreateUpdateSerializer


class UserUpdateView(generics.RetrieveUpdateAPIView):
    """ Update user """
    queryset = User.objects.all()
    serializer_class = UserCreateUpdateSerializer


class UserDestroyView(generics.RetrieveDestroyAPIView):
    """ Delete user """
    queryset = User.objects.all()
    serializer_class = UserDefaultSerializer


class LandlordRetrieveView(generics.RetrieveAPIView):
    """ Get information about specific landlord """
    queryset = Landlord.objects.all()
    serializer_class = LandlordSerializer


class LandlordListView(generics.ListAPIView):
    """ Get landlord list """
    queryset = Landlord.objects.all()
    serializer_class = LandlordSerializer


class LandlordCreateView(generics.CreateAPIView):
    """ Create landlord """
    queryset = Landlord.objects.all()
    serializer_class = LandlordCreateSerializer


class LandlordDestroyView(generics.RetrieveDestroyAPIView):
    """ Delete landlord """
    queryset = Landlord.objects.all()
    serializer_class = LandlordSerializer


class TenantRetrieveView(generics.RetrieveAPIView):
    """ Get information about specific tenant """
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer


class TenantListView(generics.ListAPIView):
    """ Get tenant list """
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer


class TenantCreateView(generics.CreateAPIView):
    """ Create tenant """
    queryset = Tenant.objects.all()
    serializer_class = TenantCreateSerializer


class TenantDestroyView(generics.RetrieveDestroyAPIView):
    """ Delete tenant """
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer


class PropertyRetrieveView(generics.RetrieveAPIView):
    """ Get information about specific property """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class PropertyListView(generics.ListAPIView):
    """ Get property list """
    serializer_class = PropertySerializer

    def get_queryset(self):
        params = self.request.GET
        hidden = params.get('hidden')
        id = params.get('id')
        owner = params.get('owner')
        city = params.get('city')
        guests = params.get('guests')
        checkin = params.get('checkin')
        checkout = params.get('checkout')

        queryset = Property.objects.all()
        if hidden:
            queryset = queryset.filter(is_hidden=False)
        if id:
            queryset = queryset.filter(pk=id)
        if owner:
            queryset = queryset.filter(owner__pk=owner)
        if city:
            queryset = queryset.filter(city=city)
        if guests:
            queryset = queryset.filter(guest_limit__gte=int(guests))
        if checkin or checkout:
            if not checkin:
                checkout = parse_date(checkout)
                checkin = checkout - timedelta(1)
            elif not checkout:
                checkin = parse_date(checkin)
                checkout = checkin + timedelta(1)
            else:
                checkin = parse_date(checkin)
                checkout = parse_date(checkout)

            bookings = Booking.objects.filter(checkin__lte=checkin, checkout__gt=checkin) | \
                       Booking.objects.filter(checkin__lt=checkout, checkin__gte=checkin)
            bookings = bookings.filter(~Q(status='CANCELLED'))

            for booking in bookings:
                queryset = queryset.exclude(pk=booking.property.pk)

        return queryset


class PropertyCreateView(generics.CreateAPIView):
    """ Create property """
    queryset = Property.objects.all()
    serializer_class = PropertyCreateUpdateSerializer


class PropertyUpdateView(generics.RetrieveUpdateAPIView):
    """ Update property """
    queryset = Property.objects.all()
    serializer_class = PropertyCreateUpdateSerializer


class PropertyDestroyView(generics.RetrieveDestroyAPIView):
    """ Delete property """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class BookingRetrieveView(generics.RetrieveAPIView):
    """ Get information about specific booking """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class BookingListView(generics.ListAPIView):
    """ Get booking list """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_queryset(self):
        params = self.request.GET
        id = params.get('id')
        owner = params.get('owner')
        tenant = params.get('tenant')

        queryset = Booking.objects.all()
        if id:
            queryset = queryset.filter(pk=id)
        if owner:
            queryset = queryset.filter(property__owner__pk=owner)
        if tenant:
            queryset = queryset.filter(tenant__pk=tenant)

        return queryset


class BookingCreateView(generics.CreateAPIView):
    """ Create booking """
    queryset = Booking.objects.all()
    serializer_class = BookingCreateSerializer


class BookingUpdateView(generics.RetrieveUpdateAPIView):
    """ Update booking """
    queryset = Booking.objects.all()
    serializer_class = BookingUpdateSerializer


class BookingDestroyView(generics.RetrieveDestroyAPIView):
    """ Delete booking """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class ReviewRetrieveView(generics.RetrieveAPIView):
    """ Get information about specific review """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewListView(generics.ListAPIView):
    """ Get review list """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        params = self.request.GET
        booking = params.get('booking')
        property = params.get('property')

        queryset = Review.objects.all()
        if booking:
            queryset = queryset.filter(booking__pk=booking)
        elif property:
            queryset = queryset.filter(booking__property__pk=property)

        return queryset


class ReviewCreateView(generics.CreateAPIView):
    """ Create review """
    queryset = Review.objects.all()
    serializer_class = ReviewCreateUpdateSerializer


class ReviewUpdateView(generics.RetrieveUpdateAPIView):
    """ Update review """
    queryset = Review.objects.all()
    serializer_class = ReviewCreateUpdateSerializer


class ReviewDestroyView(generics.RetrieveDestroyAPIView):
    """ Delete review """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    # @swagger_auto_schema(operation_summary="review destroy header")
    # def get(self, request, *args, **kwargs):
    #     return super(self).get(request, *args, **kwargs)
