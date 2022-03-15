from django.urls import path
from .views import *


app_name = "warriors_app"


urlpatterns = [
    path('warriors/list/', WarriorListAPIView.as_view()),
    path('profession/generic_create/', ProfessionCreateAPIView.as_view()),
    path('warriors_professions/', WarriorProfessionList.as_view()),
    path('warriors_skills/', WarriorSkills.as_view()),
    path('warrior/<int:pk>/', SingleWarrior.as_view()),
    path('warrior/<int:pk>/edit/', EditWarrior.as_view()),
    path('doc/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('doc/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]