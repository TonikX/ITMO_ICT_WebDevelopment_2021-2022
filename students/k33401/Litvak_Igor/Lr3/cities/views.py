from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from cities.models import City, FavouriteCity
from cities.serializers import CitySerializer, FavouriteCitySerializer, LatLonSerializer
from cities.utils import get_external_api_response, haversine_distance


class CityViewSet(ReadOnlyModelViewSet):
    """Viewset for cities"""
    queryset = City.objects.all()
    serializer_class = CitySerializer

    @method_decorator(cache_page(60))
    @action(methods=['GET'], detail=True, url_path='forecast')
    def forecast(self, request, *args, **kwargs):
        """Cached wrapper around OpenWeatherMap API"""
        city = self.get_object()
        print(f"Calling external API for city {city.name}")
        resp = get_external_api_response(lat=city.lat, lon=city.lon)
        return Response(resp.json(), status=resp.status_code)

    @swagger_auto_schema(method='GET', query_serializer=LatLonSerializer)
    @action(methods=['GET'], detail=False, url_path='closest')
    def closest(self, request, *args, **kwargs):
        """Returns city closest to certain coordinates"""
        query_serializer = LatLonSerializer(request.query_params)
        if not query_serializer.is_valid():
            return Response(query_serializer.errors, status=400)
        lat = query_serializer.validated_data['lat']
        lon = query_serializer.validated_data['lon']
        best = min(self.queryset, key=lambda city: haversine_distance(lat, lon, city.lat, city.lon))
        return self.get_serializer_class()(best).data


class FavouriteCityViewSet(ModelViewSet):
    """Viewset for favourite cities"""
    permission_classes = [IsAuthenticated]
    queryset = FavouriteCity.objects.none()
    serializer_class = FavouriteCitySerializer

    def get_queryset(self):
        return FavouriteCity.objects.filter(user=self.request.user.id)
