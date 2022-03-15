from django.urls import path
from . import views

urlpatterns = [
    path('owner/<int:owner_id>/', views.owner),
    path('car/', views.Car_List.as_view()),
    path('car/<int:pk>/', views.One_Car.as_view()),
    path('owner_create', views.create_view),
    path('car/<int:pk>/update', views.Car_Update.as_view()),
    path('car_create', views.Car_Create.as_view()),
    path('car/<int:pk>/delete', views.Car_Delete.as_view())
]