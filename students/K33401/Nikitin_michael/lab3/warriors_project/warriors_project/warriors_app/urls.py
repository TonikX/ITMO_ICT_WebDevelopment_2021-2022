from django.urls import path
from .views import (
   ProfessionAPIView, 
   WarriorAPIView, 
   ProfessionCreateView, 
   SkillAPIView, 
   SkillCreateView, 
   WarriorDetailView, 
   WarriorProfessionListAPIView, 
   WarriorSkillListAPIView,
   OneWarriorUpdateAPIView,
)


app_name = "warriors_app"


urlpatterns = [
   path('warriors/', WarriorAPIView.as_view()),
   path('warrior/<int:pk>/', WarriorDetailView.as_view()),
   path('warrior/<int:pk>/update/', OneWarriorUpdateAPIView.as_view()),
   path('professions/', ProfessionAPIView.as_view()),
   path('profession/create/', ProfessionCreateView.as_view()),
   path('skills/', SkillAPIView.as_view()),
   path('skill/create/', SkillCreateView.as_view()),
   path('warriors_profession/', WarriorProfessionListAPIView.as_view()),
   path('warriors_skill/', WarriorSkillListAPIView.as_view()),
]
