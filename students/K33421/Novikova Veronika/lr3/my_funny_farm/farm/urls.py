from django.urls import path
from .views import *

app_name = "farm"

urlpatterns = [
    path('users/list/', UserListAPIView.as_view()),
    path('users/info/<int:pk>', UserInfoAPIView.as_view()),
    #path('users/create/', UserCreateAPIView.as_view()),

    path('chickens/list/', ChickenListAPIView.as_view()),
    path('chickens/info/<int:pk>', ChickenInfoAPIView.as_view()),
    path('chickens/create/', ChickenCreateAPIView.as_view()),

    path('breeds/list/', BreedListAPIView.as_view()),
    path('breeds/info/<int:pk>', BreedInfoAPIView.as_view()),
    path('breeds/create/', BreedCreateAPIView.as_view()),

    path('work/list/', WorkListAPIView.as_view()),
    path('work/info/<int:pk>', WorkInfoAPIView.as_view()),
    path('work/create/', WorkCreateAPIView.as_view()),

    path('cage/list/', CageListAPIView.as_view()),
    path('cage/info/<int:pk>', CageInfoAPIView.as_view()),
    path('cage/create/', CageCreateAPIView.as_view()),


 ]
