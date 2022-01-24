from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.mixins import RetrieveModelMixin

from .filters import DailyFilterSet
from .serializers import *


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    # @action(detail=True, methods=['GET'], filter_backends=[DjangoFilterBackend])
    # def daily(self, request, *args, **kwargs):
    #     pass


class CityDailyViewSet(ListAPIView):
    queryset = WeatherDaily.objects.all()
    serializer_class = CityDailySerializer

    filterset_class = DailyFilterSet
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        return super().get_queryset().filter(Forecast__city_id=self.kwargs['id'])


class ForecastViewSet(viewsets.ModelViewSet):
    queryset = WeatherForecast.objects.all()
    serializer_class = ForecastSerializer
