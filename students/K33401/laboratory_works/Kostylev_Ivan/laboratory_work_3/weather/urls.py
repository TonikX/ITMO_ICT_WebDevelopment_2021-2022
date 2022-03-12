from django.urls import path

from weather.views import CreateUserAPIView, UserAPIView, GetUserInfoAPIView, UpdateUserAPIView, \
    CreateTownAPIView, CreateCountryAPIView, GetTownsAPIView, GetCountriesAPIView

app_name = "warriors_app"


urlpatterns = [
    path('user/create/', CreateUserAPIView.as_view()),
    path('user/all/', UserAPIView.as_view()),
    path('user/<int:pk>/', GetUserInfoAPIView.as_view()),
    path('user/<int:pk>/update/', UpdateUserAPIView.as_view()),
    path('town/all/', GetTownsAPIView.as_view()),
    path('town/create/', CreateTownAPIView.as_view()),
    path('country/create/', CreateCountryAPIView.as_view()),
    path('country/all/', GetCountriesAPIView.as_view())
]
