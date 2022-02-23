from django.views.generic import DetailView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, RetrieveAPIView, UpdateAPIView

from weather.models import User, Country, Town
from weather.serializers import UserSerializer, TownSerializer, CountrySerializer


class CreateUserAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class GetUserInfoAPIView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UpdateUserAPIView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CreateCountryAPIView(CreateAPIView):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()


class GetCountriesAPIView(RetrieveAPIView):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()


class CreateTownAPIView(CreateAPIView):
    serializer_class = TownSerializer
    queryset = Town.objects.all()


class GetTownsAPIView(RetrieveAPIView):
    serializer_class = TownSerializer
    queryset = Town.objects.all()
