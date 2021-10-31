from django.urls import path
from .views import *

urlpatterns = [
    path('user/', detail),
    path('user/<id>', detail_view),
    path('create/', CreateView),
    path('time/', TimeView)
]