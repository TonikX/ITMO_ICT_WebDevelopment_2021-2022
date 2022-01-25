from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('project_first_app.urls')), #данная строчка импортирует в проект отдельный файл юрлов Вашего приложения (example6_app - название Вашего приложения (название папки)), urls указывает на файл юрлов в папке приложения (указывает на тот пустой файл, который мы создали в пункте 9.а.
]

