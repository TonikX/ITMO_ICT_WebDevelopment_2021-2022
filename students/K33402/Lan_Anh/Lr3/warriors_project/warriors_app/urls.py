from django.urls import path
from .views import *

app_name = "warriors_app"

urlpatterns = [
   path('warriors/', WarriorAPIView.as_view()),
   path('warriors/list/', WarriorListAPIView.as_view()),
   path('profession/create/', ProfessionCreateView.as_view()),
   path('profession/generic_create/', ProfessionCreateAPIView.as_view()),
   path('skills/', SkillAPIView.as_view()),
   path('skills/create/', SkillCreateView.as_view()),

   # Prac 3.1
   path('warriors_skills/', WarriorSkillListAPIView.as_view()),
   path('warriors_profession/', WarriorProfessionListAPIView.as_view()),
   path('warriors/<int:pk>', WarriorSingleRetrieveAPIView.as_view()),
   path('warriors/delete/<int:pk>', WarriorSingleDestroyAPIView.as_view()),
   path('warriors/update/<int:pk>', WarriorSingleUpdateAPIView.as_view()),
]