from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView

class WarriorAPIView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorSerializer(warriors, many=True)
        return Response({"Warriors": serializer.data})

class WarriorCreateAPIView(CreateAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()
    # permission_classes = [permissions.AllowAny]

class ProfessionCreateView(CreateAPIView):
    serializer_class = ProfessionCreateSerializer
    # def post(self, request):
    #     profession = request.data

    #     serializer = ProfessionCreateSerializer(data=profession)

    #     if serializer.is_valid(raise_exception=True):
    #         profession_saved = serializer.save()

    #     return Response({"Success": "Profession '{}' created succesfully.".format(profession_saved.title)})

    # def get(self, request):
    #     profession = Profession.objects.all()
    #     serializer = ProfessionCreateSerializer(profession, many=True)
    #     return Response({"Professions": serializer.data})
    queryset = Profession.objects.all()

class SkillCreateView(APIView):
    def post(self, request):
        print(request.data)
        skill = request.data.get('skill')

        serializer = SkillCreateSerializer(data=skill)

        if serializer.is_valid(raise_exception=True):
            skill_saved = serializer.save()

        return Response({"Success": "Skill '{}' created succesfully.".format(skill_saved.title)})

    def get(self, request):
        skill = Skill.objects.all()
        serializer = SkillCreateSerializer(skill, many=True)
        return Response({"Skill": serializer.data})

class SkillView(APIView):

    def get(self, request):
        skill = Skill.objects.all()
        serializer = SkillCreateSerializer(skill, many=True)
        return Response({"Skill": serializer.data})

class WarriorSkillAPIView(APIView):
    def get(self, request):
       warriors = Warrior.objects.all()
       serializer = WarriorSkillSerializer(warriors, many=True)
       return Response({"Warrior's skill": serializer.data})

class WarriorProfessionAPIView(APIView):
    def get(self, request):
       warriors = Warrior.objects.all()
       serializer = WarriorProfessionSerializer(warriors, many=True)
       return Response({"Warrior's profession": serializer.data})

class WarriorID(RetrieveAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorIDSerializer

class WarriorDelete(DestroyAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer

class WarriorUpdate(UpdateAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorIDSerializer 
