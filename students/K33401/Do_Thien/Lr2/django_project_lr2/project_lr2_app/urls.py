from django.urls import path
from .views import *

urlpatterns = [
    path('rooms/', RoomListView),
    path('rooms/<id>', DetailRoomView),
    path('book/', BookRoom),
    path('user/', UserListView),
    path('user/<id>', DetailUserView),
    path('create/', CreateUser),
    path('comment/', Comment),
    path('bill/', BillListView),
    path('bill/<int:pk>/update/', UpdateBill.as_view()),
    path('bill/<int:pk>/delete/', DeleteBill.as_view()),
    path('lastmonth/', ListUserLastMonth)
]