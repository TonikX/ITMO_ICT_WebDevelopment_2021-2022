from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class WarriorListView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorSerializer(warriors, many=True)
        return Response({"Warriors": serializer.data})


class ProfessionCreateView(APIView):
    def post(self, request):
        profession = request.data.get("profession")
        serializer = ProfessionSerializer(data=profession)

        if serializer.is_valid(raise_exception=True):
            profession_saved = serializer.save()

        return Response({"Success": "Profession '{}' created succesfully.".format(profession_saved.title)})


class SkillCreateView(APIView):
    def post(self, request):
        skill = request.data.get("skill")
        serializer = SkillSerializer(data=skill)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response({"Success": "Created successfully."})


class WarriorCreateView(generics.CreateAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


class ProfessionView(APIView):
    def get(self, request):
        prof = Profession.objects.all()
        serializer = ProfessionSerializer(prof, many=True)
        return Response({"Profession": serializer.data})


class SkillView(APIView):
    def get(self, request):
        skill = Skill.objects.all()
        serializer = SkillSerializer(skill, many=True)
        return Response({"Skill": serializer.data})


class WarriorSkillCreateView(generics.CreateAPIView):
    serializer_class = WarriorSkillSerializer
    queryset = SkillOfWarrior.objects.all()


class WarriorsSkills(APIView):
    def get(self, request):
        skill = Warrior.objects.all()
        serializer = WarriorSkillsSerializer(skill, many=True)
        return Response({"Skill": serializer.data})


class WarriorsProfessions(APIView):
    def get(self, request):
        prof = Warrior.objects.all()
        serializer = WarriorProfSerializer(prof, many=True)
        return Response({"Professions": serializer.data})


class SingleWarriorView(generics.RetrieveAPIView):
    serializer_class = SingleWarriorSerializer
    queryset = Warrior.objects.all()


class WarriorUpdateView(generics.UpdateAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()
    lookup_field = 'pk'


class WarriorDestroyView(generics.DestroyAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer
