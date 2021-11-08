from django.urls import path
from .views import *

urlpatterns = [
    path('', Homepage.as_view()),
    path('login/', login_, name='login'),
    path('register/', register, name="register"),
    path('logout/', logout_, name='logout'),
    path('tasks/', ListTasks.as_view()),
    path('tasks/<int:pk>', Assignment.as_view()),
    path('finished/', FinishedTasks.as_view()),
    path('finished/<int:pk>/add/', AddEntry.as_view(success_url="/finished/")),
    path('finished/<int:pk>/update/', UpdateEntry.as_view(success_url="/finished/")),
    path('finished/<int:pk>/delete/', DeleteEntry.as_view(success_url="/finished/")),
    path('grades/', Grades.as_view()),
]

