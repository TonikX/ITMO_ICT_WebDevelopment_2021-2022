from django.urls import path
from .views import *


app_name = "warriors_app"


urlpatterns = [
   path('warriors/', WarriorAPIView.as_view()),
   path('profession/create/', ProfessionCreateView.as_view()),
   path('skill/create/', SkillCreateView.as_view()),
   path('skill/', SkillView.as_view()),
   path('warriors/skills/', WarriorSkillAPIView.as_view()),
   path('warriors/professions/', WarriorProfessionAPIView.as_view()),
   path('warriors/<int:pk>/', WarriorID.as_view()),
   path('warriors/delete/<int:pk>/', WarriorDelete.as_view()),
   path('warriors/create/', WarriorCreateAPIView.as_view()),
   path('warriors/update/<int:pk>/', WarriorUpdate.as_view()),
]