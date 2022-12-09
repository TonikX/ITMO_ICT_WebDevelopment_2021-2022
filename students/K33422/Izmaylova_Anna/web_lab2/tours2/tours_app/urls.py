from django.urls import path
from .view_create_user import * 
from .view_bookings import *
from .view_review import * 
from .view_tours import *  

urlpatterns = [
    path('user/register/', UserCreateView.as_view()),
    path('user/login/', UserLogin.as_view(),name = "login"),

    path('tours_list/', TourList.as_view()),
    path('tour_detail/<int:pk>/', TourRetrieveView.as_view()),

    path('reviews_list/', ReviewList.as_view()),
    path('reviews/create/', ReviewCreateView.as_view()),

    path('bookings_list/', Booked.as_view()),
    path('bookings_list/<int:pk>/', Booked.as_view()),
    path('bookings/create/', MakeReservation.as_view()),
    path('bookings/update/<int:pk>/', EditReservation.as_view()),
    path('bookings/delete/<int:pk>/', DeleteReservation.as_view()),

]