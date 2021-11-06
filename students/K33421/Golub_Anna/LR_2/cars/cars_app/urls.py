from django.urls import path

from .views import *

urlpatterns = [
    path('owner/<int:owner_id>/', owner),
    path('owner/list/', owner_list),
    path('owner/create', owner_create),

    path('car/<int:pk>/', CarRetrieveView.as_view()),
    path('car/list/', CarList.as_view()),
    path('car/create/', CarCreateView.as_view()),
    path('car/<int:pk>/update/', CarUpdateView.as_view()),
    path('car/<int:pk>/delete/', CarDeleteView.as_view()),
]
