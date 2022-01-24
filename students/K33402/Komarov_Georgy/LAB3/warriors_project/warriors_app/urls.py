from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter(trailing_slash=False)
router.register(r'professions', ProfessionViewSet, basename='professions')
router.register(r'skills', SkillViewSet, basename='skills')
router.register(r'warriors', WarriorViewSet, basename='warriors')

urlpatterns = router.urls
