from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TourViewSet, ReservationViewSet, ReviewViewSet

# Регистрируем пути
router = DefaultRouter()
router.register("tours", TourViewSet)
router.register("reservations", ReservationViewSet)
router.register("reviews", ReviewViewSet)

urlpatterns = [
    path("", include(router.urls))
]
