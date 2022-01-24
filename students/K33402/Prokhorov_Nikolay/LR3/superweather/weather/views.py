import requests
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView

from .filters import DailyFilterSet, CityFilterSet
from .serializers import *


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    filterset_class = CityFilterSet
    filter_backends = (DjangoFilterBackend,)

    def list(self, request, *args, **kwargs):
        if self.request.query_params.get("q"):
            qs = self.filter_queryset(self.get_queryset())
            if qs.count() == 0:
                print('[LOG] Указанный город не найден в базе. Делаю запрос...')

                response = requests.get(f'https://api.openweathermap.org/geo/1.0/direct',
                                        params={'q':     self.request.query_params["q"],
                                                'appid': '5872e91003e2b01d6324dda942b44d3b'
                                                })

                if len(response.json()) == 0:
                    raise ValidationError({'detail': 'Город не найден'})

                city = response.json()[0]

                print(f'[LOG] Получен город: {city}')

                city['name_ru'] = city['local_names']['ru']
                City.objects.create(**city)

        return super().list(request, *args, **kwargs)


class CityDailyViewSet(ListAPIView):
    queryset = WeatherDaily.objects.all()
    serializer_class = CityDailySerializer

    filterset_class = DailyFilterSet
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        return super().get_queryset().filter(forecast__city_id=self.kwargs['id'])


class CityForecastViewSet(ListAPIView):
    queryset = WeatherForecast.objects.all()
    serializer_class = ForecastSerializer

    def get_queryset(self):
        return super().get_queryset().filter(city_id=self.kwargs['id'])

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset()

        if qs.count() == 0:
            city = City.objects.get(id=self.kwargs['id'])

            print(f'[LOG] Прогноз погоды для города {city.name_ru} не найден в базе. Делаю запрос...')

            response = requests.get(f'https://api.openweathermap.org/data/2.5/onecall',
                                    params={'lat':   city.lat,
                                            'lon':   city.lon,
                                            'units': 'metric',
                                            'appid': '5872e91003e2b01d6324dda942b44d3b'
                                            })

            if len(response.json()) == 0:
                raise ValidationError({'detail': 'Что-то пошло не так! Прогноз не найден'})

            forecast = response.json()

            print(f'[LOG] Получен прогноз: {forecast}')

            current = WeatherCurrent.objects.create(**forecast['current'])

            forecast['city'] = city
            forecast['current'] = current
            forecast_daily = forecast.pop('daily')

            forecast_obj = WeatherForecast.objects.create(**forecast)

            daily = []
            for dailyForecast in forecast_daily:
                dailyForecast['forecast'] = forecast_obj
                dailyForecast['weekday'] = 0
                daily.append(WeatherDaily(**dailyForecast))

            WeatherDaily.objects.bulk_create(daily)

        return super().list(request, *args, **kwargs)


class ForecastViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = WeatherForecast.objects.all()
    serializer_class = ForecastSerializer
