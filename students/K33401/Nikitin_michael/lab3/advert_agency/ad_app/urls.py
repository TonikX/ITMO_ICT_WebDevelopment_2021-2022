from django.contrib import admin
from django.urls import path, include, re_path
from .views import *
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('workers', WorkersAPI.as_view()),
    path('auth/token', obtain_jwt_token),
    path('auth/token/refresh', refresh_jwt_token),
    path('applications', ApplicationsAPI.as_view()),
    path('applications/create', ApplicationsCreateAPI.as_view()),
    path('applications/<int:pk>', ApplicationsDetailsAPI.as_view()),
    path('applications/<int:pk>/delete', ApplicationsDeleteAPI.as_view()),
    path('applications/<int:pk>/update', ApplicationsUpdateAPI.as_view()),
    path('service/create', ServiceCreateAPI.as_view()),
    path('service/<int:pk>/update', ServiceUpdateAPI.as_view()),
    path('service', ServiceAPI.as_view()),
    path('service/<int:pk>/delete', ServiceDeleteAPI.as_view()),
    path('service/<int:pk>', ServiceDetailsAPI.as_view()),
    path('assignment/create', AssignmentCreateAPI.as_view()),
    path('assignment/<int:pk>/update', AssignmentUpdateAPI.as_view()),
    path('assignment', AssignmentAPI.as_view()),
    path('assignment/<int:pk>/delete', AssignmentDeleteAPI.as_view()),
    path('assignment/<int:pk>', AssignmentDetailsAPI.as_view()),
]