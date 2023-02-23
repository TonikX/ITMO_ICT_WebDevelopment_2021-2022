from django.urls import path
from .views import *

urlpatterns = [
    path('cities/', CityAPIView.as_view()),
    path('cities/create', CityCreateView.as_view()),
    
    path('favourites/', FavouriteAPIView.as_view()),
    path('favourites/create', FavouriteCreateView.as_view()),
    path('favourites/delete', FavouriteDeleteView.as_view()),

    path('users/', UserAPIView.as_view()),
]
