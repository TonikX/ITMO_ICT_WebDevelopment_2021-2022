from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    path("user/list/", user_list),
    path("user/create/", user_create),
    path("places/list/", places_list),
    path("reserve_place/", ReservePlace.as_view()),
    path("comment/", comment),
    path('flight/<int:pk>', PassengerList.as_view()),
    path("reserve/list/", reserv_list),
    path("reserve/<int:pk>/update/", ReservationUpdate.as_view()),
    path("reserve/<int:pk>/delete/", ReservationDelete.as_view()),
    path("mainpage/", mainpage), 
    url("search/", ESearchView.as_view(), name="index")
]
