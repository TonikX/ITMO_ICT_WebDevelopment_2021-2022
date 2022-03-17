from django.urls import path
from .views import *


app_name = "warriors_app"


urlpatterns = [
   path('warriors/', WarriorAPIView.as_view()),
   path('profession/create/', ProfessionCreateView.as_view()),
   path('skill/create/', SkillCreateView.as_view()),
   path('warriors/list/', WarriorListAPIView.as_view()),
   path('warriors/generic_create/', WarriorCreateAPIView.as_view()),
   path('profession/generic_create/', ProfessionCreateAPIView.as_view()),
   path('warriors_professions/', WarriorProfessionList.as_view()),
   path('warriors_skills/', WarriorSkills.as_view()),
   path('warriors/<int:pk>/', SingleWarrior.as_view()),
   path('warriors/<int:pk>/edit/', EditWarrior.as_view()),
   ]