from django.urls import path
from .views import *

urlpatterns = [
    path('owner/', detail),
    path('owner/<id>/', detail_view),
    path('time/', example_view),
    path('car/', ExampleList.as_view()),
    path('car/<int:pk>/', CarRetrieveView.as_view()),
    path('car/list/', CarListView.as_view()),
    path('owner/create/', CreateViewCar),
    path('car/<int:pk>/update/', CarUpdateView.as_view()),
    path('car/create/', CarCreateView.as_view(success_url="/car/")),
    path('car/<int:pk>/delete/', CarDeleteView.as_view()),
]
