from django.urls import path
from .views import *

urlpatterns = [
    path('city/', CityView.as_view()),
]