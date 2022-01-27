from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cities.views import CityViewSet, FavouriteCityViewSet

router = DefaultRouter()
router.register('favourite', FavouriteCityViewSet)
router.register('', CityViewSet)

urlpatterns = [
    path('', include(router.urls))
]
