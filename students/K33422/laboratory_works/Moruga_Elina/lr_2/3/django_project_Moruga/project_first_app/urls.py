from django.urls import path 
from . import views, views_func, views_class, views_forms_func, views_form_class #подключение файла контроллеров,описанного в пункте 3
urlpatterns = [
    
    path('owners/<int:owner_id>/', views.detail), #пример вызова контроллера (функции) с именем "year_archive" из файда views и передачи в него переменной "year"
    path('owners_list_func/', views_func.list_view),
    path('cars/list/', views_class.CarList.as_view()),
    path('cars/<int:pk>/', views_class.CarRetrieveView.as_view()), # ?
    path('owner_create_form', views_forms_func.create_view),
    path('cars/<int:pk>/update/', views_form_class.CarsUpdateView.as_view()),
    path('cars/create/', views_form_class.CarCreateView.as_view()),
    path('cars/<int:pk>/delete/', views_form_class.CarDeleteView.as_view()),
]
