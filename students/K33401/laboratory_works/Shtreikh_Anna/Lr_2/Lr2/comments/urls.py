from django.urls import path
from . import views

urlpatterns = [
    path('hotel/<int:h_id>/room_list/room/<int:r_id>/comments/', views.comments),
]
