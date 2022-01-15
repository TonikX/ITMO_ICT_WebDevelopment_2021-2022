from django.db.models import query
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='v2',
      description="Description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="hardbeat34@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

class WarriorListAPIView(generics.ListAPIView):
   serializer_class = WarriorSerializer
   queryset = Warrior.objects.all()

class ProfessionCreateAPIView(generics.CreateAPIView):
   serializer_class = ProfessionCreateSerializer
   queryset = Profession.objects.all()

class WarriorProfessionList(generics.ListAPIView):
    serializer_class = WarriorProfessionSerializer
    queryset = Warrior.objects.all() 

class WarriorSkills(generics.ListAPIView):
   serializer_class = WarriorRelatedSerializer
   queryset = Warrior.objects.all()

class SingleWarrior(generics.RetrieveAPIView):
   serializer_class = WarriorProfessionSkillSerializer
   queryset = Warrior.objects.all()

class EditWarrior(generics.RetrieveUpdateDestroyAPIView):
   serializer_class = WarriorSerializer
   queryset = Warrior.objects.all()