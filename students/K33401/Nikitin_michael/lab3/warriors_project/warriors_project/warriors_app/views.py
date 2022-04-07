from django.shortcuts import render
from rest_framework import serializers, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import (
    Profession,
    Warrior,
    Skill
)
from .serializers import (
    ProfessionSerializer, 
    SkillCreateSerializer, 
    WarriorDetailSerializer, 
    WarriorProfessionSerializer, 
    WarriorSerializer, 
    ProfessionCreateSerializer, 
    SkillSerializer, 
    WarriorSkillSerializer
    )

# Create your views here.
class WarriorAPIView(APIView):
	def get(self, request):
		warriors = Warrior.objects.all()
		serializer = WarriorSerializer(warriors, many=True)
		return Response({"Warriors": serializer.data})


class WarriorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WarriorDetailSerializer
    queryset = Warrior.objects.all()



class ProfessionAPIView(APIView):
    def get(self, request):
        professions = Profession.objects.all()
        serializer = ProfessionSerializer(professions, many=True)
        return Response({"Professions": serializer.data})


class ProfessionCreateView(generics.CreateAPIView):
    serializer_class = ProfessionCreateSerializer
    queryset = Profession.objects.all()


class SkillAPIView(APIView):    
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response({"Skills": serializer.data})


class SkillCreateView(APIView):

   def post(self, request):
       skill = request.data.get("skill")
       serializer = SkillCreateSerializer(data=skill)

       if serializer.is_valid(raise_exception=True):
           skill_saved = serializer.save()

       return Response({"Success": "Skill '{}' created succesfully.".format(skill_saved.title)})


class WarriorProfessionListAPIView(generics.ListAPIView):
   serializer_class = WarriorProfessionSerializer
   queryset = Warrior.objects.all()


class WarriorSkillListAPIView(generics.ListAPIView):
    serializer_class = WarriorSkillSerializer
    queryset = Warrior.objects.all()


class OneWarriorUpdateAPIView(generics.UpdateAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()
    lookup_field = 'pk'