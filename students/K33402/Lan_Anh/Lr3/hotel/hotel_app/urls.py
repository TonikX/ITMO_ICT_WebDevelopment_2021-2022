from django.urls import path
from .views import *

app_name = "hotel_app"

urlpatterns = [
    # Visitors CRUD
    path('visitors/', VisitorListView.as_view()),
    path('visitors/<int:pk>', VisitorSingleRetrieveView.as_view()),
    path('visitors/<int:pk>/update', VisitorSingleUpdateView.as_view()),
    path('visitors/<int:pk>/destroy', VisitorSingleDestroyView.as_view()),

    # -----

    # Hosts CRUD
    path('hosts/', HostListView.as_view()),
    path('hosts/<int:pk>', HostSingleRetrieveView.as_view()),
    path('hosts/<int:pk>/update', HostSingleUpdateView.as_view()),
    path('hosts/<int:pk>/destroy', HostSingleDestroyView.as_view()),
    # -----

    # Hotels CRUD
    path('hotels/', HotelListView.as_view()),
    path('hotels/create', HotelSingleCreateView.as_view()),
    path('hotels/<int:pk>', HotelSingleRetrieveView.as_view()),
    path('hotels/<int:pk>/update', HotelSingleUpdateView.as_view()),
    path('hotels/<int:pk>/destroy', HotelSingleDestroyView.as_view()),

    # -----

    # Rooms CRUD
    path('rooms/', RoomListView.as_view()),
    path('rooms/create', RoomSingleCreateView.as_view()),
    path('rooms/<int:pk>', RoomSingleRetrieveView.as_view()),
    path('rooms/<int:pk>/update', RoomSingleUpdateView.as_view()),
    path('rooms/<int:pk>/destroy', RoomSingleDestroyView.as_view()),
    # ----

    # Bookings CRUD
    path('bookings/', BookingListView.as_view()),
    path('bookings/create', BookingSingleCreateView.as_view()),
    path('bookings/<int:pk>', BookingSingleRetrieveView.as_view()),
    path('bookings/<int:pk>/update', BookingSingleUpdateView.as_view()),
    path('bookings/<int:pk>/destroy', BookingSingleDestroyView.as_view()),
    # ----

    # Bills CRUD
    path('bills/', BillListView.as_view()),
    path('bills/create', BillSingleCreateView.as_view()),
    path('bills/<int:pk>', BillSingleRetrieveView.as_view()),
    path('bills/<int:pk>/update', BillSingleUpdateView.as_view()),
    path('bills/<int:pk>/destroy', BillSingleDestroyView.as_view()),

    # ----

    # Functional Analytics
    path('bookings/<int:pk>/report', BookingReportView.as_view()),
    path('hotels/<int:pk>/info', HotelInfoView.as_view()),
    path('hotels/<int:pk>/rooms/', HotelRoomListView.as_view()),
    path('hotels/<int:pk>/rooms/available', HotelAvailableRoomListView.as_view()),
    path('visitors/<int:pk>/bookings', VisitorBookingListView.as_view())
    # ----
]