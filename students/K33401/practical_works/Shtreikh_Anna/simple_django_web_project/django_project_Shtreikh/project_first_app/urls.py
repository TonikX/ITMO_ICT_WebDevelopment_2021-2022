from django.urls import path
from . import views

urlpatterns = [
    path('owner/<int:ow_id>/', views.owner),
    path('owners_list/', views.owners_list),
    path('cars_list/', views.CarsList.as_view()),
    path('cars_list/<int:pk>', views.CarId.as_view()),
    path('owner_create', views.create_view),
    path('cars_list/<int:pk>/update', views.CarUpdate.as_view()),
    path('car_create', views.CarCreate.as_view()),
    path('cars_list/<int:pk>/delete', views.CarDelete.as_view())
]

