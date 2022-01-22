from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cities.views import CityViewSet, FavouriteCityViewSet

router = DefaultRouter()
router.register('', CityViewSet)
router.register('favourite', FavouriteCityViewSet)

urlpatterns = [
    path('', include(router.urls))
]
