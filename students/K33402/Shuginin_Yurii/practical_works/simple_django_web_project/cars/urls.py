from django.urls import path
from . import views

urlpatterns = [
    path('owner/<int:car_owner_id>/', views.car_owner_info),
]
