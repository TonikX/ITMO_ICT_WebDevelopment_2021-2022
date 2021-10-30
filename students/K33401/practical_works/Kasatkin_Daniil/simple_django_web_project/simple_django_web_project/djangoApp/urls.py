from django.urls import path
from .views import *

urlpatterns = [
    path('owner_list/<int:pk>/', OwnerRetrieveView.as_view()),
    path('owner_list/list/', OwnerListView.as_view()),
    path('owner_list/<int:pk>/update/', OwnerUpdateView.as_view()),
    path('owner_form/create/', OwnerCreateView.as_view()),
    path('owner_list/<int:pk>/delete/', OwnerDeleteView.as_view()),
]
