from django.urls import path
from . import views

urlpatterns = [
    path('hotel/<int:h_id>/', views.hotel),
    path('hotel/<int:h_id>/user_list/', views.user_list),
    path('hotel_list/', views.hotel_list),
    path('hotel/<int:h_id>/room_list/', views.room_list),
    path('hotel/<int:h_id>/room_list/room/<int:r_id>', views.room),
    path('hotel/<int:h_id>/room_list/room/<int:r_id>/reservation/', views.reservation),
    path('', views.mainpage),
    path('del_res/<int:pk>', views.DeleteReservation.as_view()),
    path('upd_res/<int:pk>', views.UpdateReservation.as_view()),
]
