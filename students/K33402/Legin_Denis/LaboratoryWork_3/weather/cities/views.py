from cities.serializers import CitySerializer, CityPreferenceReadSerializer, CityPreferenceWriteSerializer
from cities.models import City, CityPreference
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin


class CityViewSet(GenericViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()


class CityPreferenceViewSet(ListModelMixin, CreateModelMixin, DestroyModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return CityPreferenceReadSerializer
        return CityPreferenceWriteSerializer

    def get_queryset(self):
        return CityPreference.objects.filter(user=self.request.user)
