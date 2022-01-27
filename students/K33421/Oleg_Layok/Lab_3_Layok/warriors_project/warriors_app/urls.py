from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *


app_name = "warriors_app"


router = DefaultRouter()
router.register(r'warriors', WarriorAPIView)
router.register(r'skills/warriors', SkillOfWarriorAPIView)

urlpatterns = [
   path('', include(router.urls)),
   path('profession/list', ProfessionCreateAPIView.as_view()),
   path('skills/', SkillAPIView.as_view()),
]