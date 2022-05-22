from django.urls import path

from room import views

urlpatterns = [
    path('list', views.room_list, name='room-list'),
    path('create', views.create_room, name='create-room'),
    path('<int:id>', views.room, name='room'),
]
