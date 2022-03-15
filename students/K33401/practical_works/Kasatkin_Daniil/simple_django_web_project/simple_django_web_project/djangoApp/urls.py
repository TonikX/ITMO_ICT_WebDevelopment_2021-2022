from django.urls import path
from . import views

urlpatterns = [
    path('owner/<int:CarOwner_id>/', views.owner)
]
