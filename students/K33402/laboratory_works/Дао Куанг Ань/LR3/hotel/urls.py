from django.urls import path
from .views import *

urlpatterns = [
    path('bill/', BillView.as_view()),
    path('bill/create/', BillCreateAPIView.as_view()),
    path('bill/<int:pk>/update', BillUpdate.as_view()),
    path('bill/<int:pk>/delete', BillDestroy.as_view()),

    # ------------------
    path('schedule/', ScheduleView.as_view()),
    path('schedule/create/', ScheduleCreateAPIView.as_view()),
    path('schedule/<int:pk>/update', BillUpdate.as_view()),
    path('schedule/<int:pk>/delete', BillDestroy.as_view()),

    # ------------------
    path('client/', ClientView.as_view()),
    path('client/create/', ClientCreateAPIView.as_view()),
    path('client/<int:pk>/update', BillUpdate.as_view()),
    path('client/<int:pk>/delete', BillDestroy.as_view()),

    # ------------------
    path('room/', RoomView.as_view()),
    path('room/create/', RoomCreateAPIView.as_view()),
    path('room/<int:pk>/update', BillUpdate.as_view()),
    path('room/<int:pk>/delete', BillDestroy.as_view()),

    # -------------------
    path('employee/', EmployeeView.as_view()),
    path('employee/create/', EmployeeCreate.as_view()),
    path('employee/<int:pk>/update', EmployeeUpdate.as_view()),
    path('employee/<int:pk>/delete', EmployeeDestroy.as_view()),
    # -----------------
    path('1/', BillAPIView.as_view()),
    path('2/', ClientCount.as_view()),
    path('3/', EmployeeAPIView.as_view()),
    path('4/', AvailableRoomAPIView.as_view()),
    path('5/', RoomCount.as_view()),
]
