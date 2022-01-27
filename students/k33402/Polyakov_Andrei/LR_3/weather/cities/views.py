from django.shortcuts import render
from cities.serializers import CitySeriazlier, CityPreferenceReadSeriazlier, CityPreferenceWriteSeriazlier
from cities.models import City, CityPreference
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin


class CityViewSet(GenericViewSet):
    serializer_class = CitySeriazlier
    queryset = City.objects.all()

class CityPreferenceViewSet(ListModelMixin, CreateModelMixin, DestroyModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return CityPreferenceReadSeriazlier
        return CityPreferenceWriteSeriazlier

    def get_queryset(self):
        return CityPreference.objects.filter(user=self.request.user)