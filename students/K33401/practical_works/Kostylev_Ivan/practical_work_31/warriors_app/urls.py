from django.urls import path

from warriors_app.views import WarriorAPIView, ProfessionCreateView

app_name = "warriors_app"

urlpatterns = [
    path('warriors/', WarriorAPIView.as_view()),
    path('professions/create/', ProfessionCreateView.as_view())
]
