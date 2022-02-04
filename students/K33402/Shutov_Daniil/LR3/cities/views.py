from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from cities.serializers import CitySeriazlier, CityPreferenceReadSeriazlier, CityPreferenceWriteSeriazlier
from cities.models import City, CityPreference


class CityViewSet(ReadOnlyModelViewSet):
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

    # def perform_create(self, serializer):
    #     serializer.validated_data['user'] = self.request.user
    #     super(CityPreferenceViewSet, self).perform_create(serializer)
