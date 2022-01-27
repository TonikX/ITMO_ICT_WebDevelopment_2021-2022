from django.urls import path

from tickets.views import (CreateBookingView, FlightDetailView, FlightListView,
                           MyBookingsView)

urlpatterns = [
    path('', FlightListView.as_view()),
    path('<int:pk>', FlightDetailView.as_view()),
    path('bookings', CreateBookingView.as_view()),
    path('my-bookings', MyBookingsView.as_view())
]
