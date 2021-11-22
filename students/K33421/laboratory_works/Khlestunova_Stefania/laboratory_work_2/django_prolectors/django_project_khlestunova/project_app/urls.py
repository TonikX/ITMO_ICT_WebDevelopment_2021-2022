from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    path("user/list/", user_list),
    path("user/create/", user_create),
    path("places/list/", Places_List.as_view()),
    path("reserve_place/", reserve_place),
    path("comment/", comment),
    path("reserve/list/", reserv_list),
    path("reserve/<int:pk>/update/", ReservationUpdate.as_view()),
    path("reserve/<int:pk>/delete/", ReservationDelete.as_view()),
    path("mainpage/", mainpage), 
    url("search/", ESearchView.as_view(), name="index")
]
