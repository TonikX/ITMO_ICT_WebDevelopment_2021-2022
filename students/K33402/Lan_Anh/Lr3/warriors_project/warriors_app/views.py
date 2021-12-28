from django.shortcuts import render

from rest_framework.views import APIView, Response
from rest_framework import generics

from .serializers import *
from .models import Skill, Warrior


# Create your views here.
class WarriorAPIView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorSerializer(warriors, many=True)
        return Response({"Warriors": serializer.data})

class WarriorListAPIView(generics.ListAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()

class WarriorSingleRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()

class WarriorSingleDestroyAPIView(generics.DestroyAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()

class WarriorSingleUpdateAPIView(generics.UpdateAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()

class WarriorSkillListAPIView(generics.ListAPIView):
    serializer_class = WarriorSkillSerializer
    queryset = Warrior.objects.all()

class WarriorProfessionListAPIView(generics.ListAPIView):
    serializer_class = WarriorProfessionSerializer
    queryset = Warrior.objects.all()

class ProfessionCreateView(APIView):
    def post(self, request):
        profession = request.data.get("profession")
        serializer = ProfessionCreateSerializer(data=profession)

        if serializer.is_valid(raise_exception=True):
            profession_saved = serializer.save()

        return Response({"Success": "Profession '{}' created succesfully.".format(profession_saved.title)})

class ProfessionCreateAPIView(generics.CreateAPIView):
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
