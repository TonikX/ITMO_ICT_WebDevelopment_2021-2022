from django.urls import path 
from . import views #подключение файла контроллеров,описанного в пункте 3
urlpatterns = [
    
    path('owners/<int:owner_id>', views.detail), #пример вызова контроллера (функции) с именем "year_archive" из файда views и передачи в него переменной "year"
]