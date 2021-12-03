from django.urls import path
from . import views

urlpatterns = [
    path('', views.ESearchView.as_view(), name='index')
]
