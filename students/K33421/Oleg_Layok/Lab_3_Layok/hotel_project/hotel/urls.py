from django.urls import path, include
from rest_framework.routers import DefaultRouter

from hotel.views import RoomAPIView, GuestAPIView, StaffAPIView, CleaningAPIView

router = DefaultRouter()
router.register(r'rooms', RoomAPIView)
router.register(r'guests', GuestAPIView)
router.register(r'staff', StaffAPIView)
router.register(r'cleaning', CleaningAPIView)

urlpatterns = [
    path('', include(router.urls))
]
