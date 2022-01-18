from django.urls import path
from .views import *

app_name = "worriors_app"

urlpatterns = [
    path('warriors/', WarriorAPIView.as_view()),
    path('warriors/create/', WarriorsCreateView.as_view()),
    path('warriors/<int:pk>/', WarriorRetrieveAPIView.as_view()),
    path('warriors/update/<int:pk>/', WarriorUpdateAPIView.as_view()),
    path('warriors/delete/<int:pk>/', WarriorDeleteAPIView.as_view()),
    path('warriors/profession/', WarriorsProfessionView.as_view()),
    path('warriors/skills/', WarriorsSkillView.as_view()),
    path('warriors/skills/create/', SkillOfWarriorAPIView.as_view()),
    path('warriors/list/', WarriorListAPIView.as_view()),
    path('skills/', SkillAPIView.as_view()),
    path('skills/create/', SkillCreateView.as_view()),
    path('profession/create/', ProfessionCreateView.as_view()),
    path('profession/generic_create/', ProfessionCreateAPIView.as_view()),
    path('skills/generic_create/', SkillsCreateAPIView.as_view())
]