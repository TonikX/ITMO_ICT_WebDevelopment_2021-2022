from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from rest_framework.exceptions import ValidationError
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
import requests
from rest_framework.response import Response

from .serializers import *


class CityListView(mixins.ListModelMixin, GenericAPIView):
    serializer_class = CitySerializer
    queryset = CityModel.objects.all()

    def get(self, request, *args, **kwargs):
        search = self.request.query_params.get('search', None)

        if search:
            cities = CityModel.objects.filter(Q(name=search) | Q(local_names__ru=search))

            if len(cities) == 0:
                params = {'q': search, 'appid': '5ae749cc2df923e8e65a27f4fdc3eccf'}
                response = requests.get(f'https://api.openweathermap.org/geo/1.0/direct', params=params)

                if len(response.json()) == 0:
                    raise ValidationError({'error': 'Город не найден'})

                city = CityModel.objects.create(**response.json()[0])
            else:
                city = cities.first()

            serializer = self.get_serializer(city)
            return Response(serializer.data)

        return self.list(request, *args, **kwargs)


class CityItemView(mixins.RetrieveModelMixin, GenericAPIView):
    serializer_class = CitySerializer
    queryset = CityModel.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class WeaherListView(mixins.ListModelMixin, GenericAPIView):
    serializer_class = WeatherSerializer
    queryset = WeatherModel.objects.all()

    def get(self, request, *args, **kwargs):
        city = self.request.query_params.get('city', None)

        if city:
            weather_list = WeatherModel.objects.filter(city_id=int(city))
            city_object = CityModel.objects.get(id=int(city))

            if len(weather_list) == 0:
                params = {'lat':     city_object.lat, 'lon': city_object.lon, 'units': 'metric',
                          'exclude': 'hourly,minutely,alerts', 'appid': '5ae749cc2df923e8e65a27f4fdc3eccf'}
                response = requests.get(f'https://api.openweathermap.org/data/2.5/onecall', params=params)

                if len(response.json()) == 0:
                    raise ValidationError({'error': 'Что-то пошло не так! Прогноз не найден'})

                data = response.json()
                weather = WeatherModel.objects.create(city=city_object, lat=data['lat'], lon=data['lon'],
                                                      current=data['current'], daily=data['daily'])
            else:
                weather = weather_list.first()

            serializer = self.get_serializer(weather)
            return Response(serializer.data)

        return super().list(request, *args, **kwargs)


class WeatherItemView(mixins.RetrieveModelMixin, GenericAPIView):
    serializer_class = WeatherSerializer
    queryset = WeatherModel.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class MyCityView(mixins.ListModelMixin, GenericAPIView):
    serializer_class = MyCityFullSerializer
    queryset = MyCitiesModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class MyCityEditView(mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     GenericAPIView):
    serializer_class = MyCitySerializer
    queryset = MyCitiesModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
