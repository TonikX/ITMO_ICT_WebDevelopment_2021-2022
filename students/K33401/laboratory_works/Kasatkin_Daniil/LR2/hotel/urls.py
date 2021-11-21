from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('rooms', views.rooms, name='rooms'),
    path('room/<str:pk>', views.room, name='room'),
    path('reservation/<str:pk>', views.reservation, name='reservation'),
    path('profile', views.profile, name='book_list'),
    path('delete_res/<str:pk>', views.delete_reservation, name='delete_reservation'),
    path('edit_res/<str:pk>', views.edit_reservation, name='edit_reservation'),
    path('comment/<str:pk>', views.add_comment, name='add_comment'),
    path('lastmonth', views.show_last_month, name='last_month')
]
