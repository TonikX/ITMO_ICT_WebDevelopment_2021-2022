from django.urls import path
from . import views

urlpatterns = [
    path('owner/<int:owner_id>/', views.get_owner_by_id),
    path('owner/list/', views.get_owners),
    path('owner/create', views.create_owner),
    path('car/<int:pk>/', views.CarRetrieveView.as_view()),
    path('car/list/', views.CarListView.as_view()),
    path('car/<int:pk>/update/', views.CarUpdateView.as_view()),
    path('car/create/', views.CarCreateView.as_view()),
    path('car/<int:pk>/delete/', views.CarDeleteView.as_view()),
]
