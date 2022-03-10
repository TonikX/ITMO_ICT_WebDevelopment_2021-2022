from django.urls import path
from .views import *

urlpatterns = [
    path('passengers/', PassengerListView.as_view()),
    path('passengers/create/', PassengerCreateView.as_view()),
    path('passengers/<int:pk>/', PassengerEditView.as_view()),
    path('planes/', PlaneListView.as_view()),
    path('planes/create/', PlaneCreateView.as_view()),
    path('planes/<int:pk>/', PlaneEditView.as_view()),
    path('flights/', FlightListView.as_view()),
    path('flights/create/', FlightCreateView.as_view()),
    path('flights/<int:pk>/', FlightEditView.as_view()),
    path('airlines/', AirCompanyListView.as_view()),
    path('airlines/create/', AirCompanyCreateView.as_view()),
    path('airlines/<int:pk>/', AirCompanyEditView.as_view()),
    path('tickets/', TicketListView.as_view()),
    path('tickets/create/', TicketCreateView.as_view()),
    path('tickets/<int:pk>/', TicketEditView.as_view())
]