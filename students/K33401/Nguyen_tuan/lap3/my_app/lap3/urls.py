from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('staff/all', StaffListView.as_view()),
    path('staff/<int:pk>', StaffRetrieveView.as_view()),
    path('staff/update/<int:pk>', StaffUpdateView.as_view()),
    path('staff/new', StaffCreateView.as_view()),
    path('staff/delete/<int:pk>', StaffRetrieveView.as_view()),

    path('room/all', RoomListView.as_view()),
    path('room/<int:pk>', RoomRetrieveView.as_view()),
    path('room/update/<int:pk>', RoomUpdateView.as_view()),
    path('room/new', RoomCreateView.as_view()),
    path('room/delete/<int:pk>', RoomRetrieveView.as_view()),

    path('guest/all', GuestListView.as_view()),
    path('guest/<int:pk>', GuestRetrieveView.as_view()),
    path('guest/update/<int:pk>', GuestUpdateView.as_view()),
    path('guest/new', GuestCreateView.as_view()),
    path('guest/delete/<int:pk>', GuestRetrieveView.as_view()),

    path('schedule/all', ScheduleListView.as_view()),
    path('schedule/<int:pk>', ScheduleRetrieveView.as_view()),
    path('schedule/update/<int:pk>', ScheduleUpdateView.as_view()),
    path('schedule/new', ScheduleCreateView.as_view()),
    path('schedule/delete/<int:pk>', ScheduleRetrieveView.as_view()),



]