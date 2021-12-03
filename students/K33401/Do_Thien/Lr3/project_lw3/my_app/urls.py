from django.urls import path, include
from .views import *


app_name = "my_app"

urlpatterns = [
    path('guests/all/', GuestListView.as_view()),
    path('guests/<int:pk>/', GuestRetrieveView.as_view()),
    path('guests/update/<int:pk>', GuestUpdateView.as_view()),
    path('guests/new/', GuestCreateView.as_view()),

    path('staffs/all/', StaffListView.as_view()),
    path('staffs/<int:pk>/', StaffRetrieveView.as_view()),
    path('staffs/update/<int:pk>', StaffUpdateView.as_view()),
    path('staffs/new/', StaffCreateView.as_view()),

    path('floors/all/', FloorListView.as_view()),
    path('floors/<int:pk>/', FloorRetrieveView.as_view()),
    path('floors/update/<int:pk>', FloorUpdateView.as_view()),
    path('floors/new/', FloorCreateView.as_view()),

    path('status/all/', StatusListView.as_view()),
    path('status/<int:pk>/', StatusRetrieveView.as_view()),
    path('status/update/<int:pk>', StatusUpdateView.as_view()),
    path('status/new/', StatusCreateView.as_view()),

    path('types/all/', TypeListView.as_view()),
    path('types/<int:pk>/', TypeRetrieveView.as_view()),
    path('types/update/<int:pk>', TypeUpdateView.as_view()),
    path('types/new/', TypeCreateView.as_view()),

    path('rooms/all/', RoomListView.as_view()),
    path('rooms/<int:pk>/', RoomRetrieveView.as_view()),
    path('rooms/update/<int:pk>', RoomUpdateView.as_view()),
    path('rooms/new/', RoomCreateView.as_view()),

    path('reservations/all/', ReservationListView.as_view()),
    path('reservations/<int:pk>/', ReservationRetrieveView.as_view()),
    path('reservations/update/<int:pk>', ReservationUpdateView.as_view()),
    path('reservations/new/', ReservationCreateView.as_view()),

    path('schedules/all/', ScheduleListView.as_view()),
    path('schedules/<int:pk>/', ScheduleRetrieveView.as_view()),
    path('schedules/update/<int:pk>', ScheduleUpdateView.as_view()),
    path('schedules/new/', ScheduleCreateView.as_view()),
]
