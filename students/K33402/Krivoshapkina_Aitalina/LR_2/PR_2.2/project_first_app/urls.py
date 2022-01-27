from django.urls import path
from . import views #подключение файла контроллеров,описанного в пункте 3
urlpatterns = [
    path('owner/', views.owner_all), #пример вызова контроллера (функции) с именем "year_archive" из файда views и передачи в него переменной "year"
    path('owner/<int:owner_id>/', views.owner_detail), #пример вызова контроллера (функции) с именем "year_archive" из файда views и передачи в него переменной "year"
    path('car/', views.CarList.as_view()),
    path('car/<int:pk>/', views.CarRetrieveView.as_view()),
    path('example_create', views.create_view),
    path('car/<int:pk>/update/', views.CarUpdateView.as_view()),
    path('car_create', views.CarCreate.as_view(success_url="/car/")),
    path('car/<int:pk>/delete/', views.CarDeleteView.as_view()),
]

