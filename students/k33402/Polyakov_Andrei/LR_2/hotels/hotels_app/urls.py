from django.urls import path
from .views import *

urlpatterns = [
    path('', Homepage.as_view()), # homepage
    path('register/', register, name='register'),  # create user
    path('login/', login_, name='login'),  # login user
    path('logout/', logout_, name='logout'), # logout

    
    path('reservation/', ListReservation.as_view()), # reservation list
    path('reservation/create/', ReservationCreateView.as_view(success_url='/reservation/')),  # create
    path('reservation/<int:pk>', ReservationRetrieveView.as_view()),  # view
    path('reservation/<int:pk>/update/', ReservationUpdateView.as_view(success_url='/reservation/')),  # edit
    path('reservation/<int:pk>/delete/', ReservationDeleteView.as_view(success_url='/reservation/')),  # delete

    path('hotel/', HotelList.as_view()), # hotel list
    path('hotel/<int:pk>', HotelRetriveView.as_view()), # view
    path('hotel/review/', ReviewCreateView.as_view(success_url='/review/')),  # write review
    path('review/', ReviewList.as_view()), # review list

    path('guests/', GuestsList.as_view()), #guests list
    ]