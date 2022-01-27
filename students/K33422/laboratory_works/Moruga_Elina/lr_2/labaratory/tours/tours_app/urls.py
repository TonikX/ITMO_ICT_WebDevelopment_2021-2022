from django.urls import path
from .views import UserCreateView, UserLogin
from .view_tours import TourList, TourRetrieveView
from .view_reviews import ReviewList
from .view_create_review import ReviewCreateView
from .view_bookings import Booked
from .view_bookings_edit import MakeReservation, DeleteReservation, EditReservation

urlpatterns = [
    path('users_create/', UserCreateView.as_view()),
    path('tours_list/', TourList.as_view()),
    path('tour_detail/<int:pk>/', TourRetrieveView.as_view()),
    path('reviews_list/', ReviewList.as_view()),
    path('reviews/create/', ReviewCreateView.as_view()),
    path('bookings_list/', Booked.as_view()),
    path('bookings/create/', MakeReservation.as_view()),
    path('bookings/update/<int:pk>/', EditReservation.as_view()),
    path('bookings/delete/<int:pk>/', DeleteReservation.as_view()),
    path('accounts/login/', UserLogin.as_view()),
    path('bookings_list/<int:pk>/', Booked.as_view()),
]