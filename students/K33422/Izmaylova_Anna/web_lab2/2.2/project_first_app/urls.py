from django.urls import path 
from . import views #подключение файла контроллеров,описанного в пункте 3
from .views_cars import CarList,CarRetrieveView,CarUpdateView,CarCreateView,CarDeleteView

urlpatterns = [
    path('owner/<int:carowner_id>/', views.detail), #пример вызова контроллера (функции) с именем "year_archive" из файда views и передачи в него переменной "year"
    path('carowner_list/', views.list_view),
    path('car_list/', CarList.as_view()),
    path('car/<int:pk>/', CarRetrieveView.as_view()),
    path('car/update/<int:pk>/', CarUpdateView.as_view()),
    path('carowner_create/', views.create_view),
    path('car/create/', CarCreateView.as_view()),
    path('car/delete/<int:pk>/', CarDeleteView.as_view()),



]

