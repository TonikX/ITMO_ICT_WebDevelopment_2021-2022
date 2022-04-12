from . import views
from django.urls import path

urlpatterns = [
    path('', views.start_page),
    path('owners/<int:owner_id>', views.get_owner_by_id),
    path('owners/all', views.get_all_owners),
    path('owners/create', views.get_new_owner),
    path('cars/', views.CarsList.as_view()),
    path('cars/create', views.CarsCreate.as_view()),
    path('cars/<int:pk>', views.CarsRead.as_view()),
    path('cars/<int:pk>/update', views.CarsUpdate.as_view()),
    path('cars/<int:pk>/delete', views.CarsDelete.as_view()),
]