from django.urls import path
from .views import *

app_name = 'warriors'

urlpatterns = [
    path('warriors/list/', WarriorListView.as_view()),
    path('warriors/create/', WarriorCreateView.as_view()),
    path('warriors/<int:pk>/', WarriorView.as_view()),
    path('warriors/<int:pk>/update/', WarriorUpdateView.as_view()),
    path('warriors/<int:pk>/delete/', WarriorDestroyView.as_view()),

    path('warriors/professions/list/', WarriorsProfessionsView.as_view()),

    path('warriors/skills/list/', WarriorsSkillsView.as_view()),
    path('warriors/skills/create/', WarriorSkillCreateView.as_view()),
    path('warriors/skills/<int:pk>/update/', WarriorSkillUpdateView.as_view()),

    path('professions/', ProfessionView.as_view()),
    path('profession/create/', ProfessionCreateView.as_view()),

    path('skills/', SkillView.as_view()),
    path('skills/create/', SkillCreateView.as_view()),

]
