from django.urls import path

from .views import list_view, create_view


urlpatterns = [
    path('', list_view),
    path('registration/', create_view),
]