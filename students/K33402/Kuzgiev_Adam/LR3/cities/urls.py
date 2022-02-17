from django.urls import path
from cities.views import ChosenCityView


urlpatterns = [
    path('<int:city_id>/', ChosenCityView.as_view())
]