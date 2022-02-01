from django.urls import path

from warriors_app.views import WarriorAPIView, ProfessionCreateView, SkillsView, SkillsCreateView, \
    WarriorProfessionView

app_name = "warriors_app"

urlpatterns = [
    path('warriors/', WarriorAPIView.as_view()),
    path('professions/create/', ProfessionCreateView.as_view()),
    path('skills/', SkillsView.as_view()),
    path('skills/create/', SkillsCreateView.as_view()),
    path('warriors/professions', WarriorProfessionView.as_view())
]
