from django.urls import path
from .views import *

urlpatterns = [
    path('owner_list/', list_view),
    path('owner_form/create/', OwnerCreateView.as_view()),
    path('cars/', CarListView.as_view()),
    path('car_form/', CarCreateView.as_view()),
    path('car_detail/<int:pk>/', CarRetrieveView.as_view()),
    path('car_form/<int:pk>/', CarUpdateView.as_view()),
    path('car/<int:pk>/delete/', CarDeleteView.as_view()),
    path('owner_create_view/', create_view),

]
