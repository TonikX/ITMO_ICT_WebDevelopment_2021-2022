from django.urls import path, include

from board.views import Home

urlpatterns = [
    path('', include('allauth.urls')),
    path('', Home.as_view(), name='home'),
]