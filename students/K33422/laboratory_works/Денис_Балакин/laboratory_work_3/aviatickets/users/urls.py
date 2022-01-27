from django.urls import path

from users.views import MyProfileView

urlpatterns = [
    path('my-profile', MyProfileView.as_view())
]
