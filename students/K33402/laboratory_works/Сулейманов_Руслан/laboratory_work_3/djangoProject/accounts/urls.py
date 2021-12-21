from django.urls import path, include
from .views import *

urlpatterns = [
    path('me/', UserViewAPI.as_view()),
    path('me/city/', UserCitytList.as_view({'post': 'create', 'get': 'list'})),
    path('me/city/<int:pk>/', UserCitytDetail.as_view({'delete': 'destroy', 'get': 'retrieve'}))
]