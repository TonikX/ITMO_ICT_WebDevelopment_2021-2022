from django.urls import path
from .views import *

app_name = "candy_app"

urlpatterns = [
    path('candies/', CandiesListAPIView.as_view()),
    path('candies/create/', CandiesCreateAPIView.as_view()),
    path('candies/<int:pk>/', CandiesRetrieveAPIView.as_view()),
    path('candies/update/<int:pk>/', CandiesRetrieveUpdateDestroyAPIView.as_view()),
    path('client/', ClientListAPIView.as_view()),
    path('client/create/', ClientCreateAPIView.as_view()),
    path('client/<int:pk>/', ClientRetrieveAPIView.as_view()),
    path('client/update/<int:pk>/', ClientRetrieveUpdateDestroyAPIView.as_view()),
    path('staff/', StaffListAPIView.as_view()),
    path('staff/create/', StaffCreateAPIView.as_view()),
    path('staff/<int:pk>/', StaffRetrieveAPIView.as_view()),
    path('staff/update/<int:pk>/', StaffRetrieveUpdateDestroyAPIView.as_view()),
    path('request/', RequestListAPIView.as_view()),
    path('request/create/', RequestCreateAPIView.as_view()),
]