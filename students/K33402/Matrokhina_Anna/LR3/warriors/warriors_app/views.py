from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *


class WarriorListView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorSerializer(warriors, many=True)
        return Response({'Warriors': serializer.data})


class WarriorView(RetrieveAPIView):
    serializer_class = SingleWarriorSerializer
    queryset = Warrior.objects.all()


class ProfessionCreateView(CreateAPIView):
    serializer_class = ProfessionSerializer
    queryset = Profession.objects.all()


class SkillCreateView(CreateAPIView):
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()


class WarriorCreateView(CreateAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


class ProfessionView(APIView):
    def get(self, request):
        prof = Profession.objects.all()
        serializer = ProfessionSerializer(prof, many=True)
        return Response({'Profession': serializer.data})


class SkillView(APIView):
    def get(self, request):
        skill = Skill.objects.all()
        serializer = SkillSerializer(skill, many=True)
        return Response({'Skill': serializer.data})


class WarriorSkillCreateView(CreateAPIView):
    serializer_class = WarriorSkillSerializer
    queryset = SkillOfWarrior.objects.all()


class WarriorSkillUpdateView(UpdateAPIView):
    serializer_class = WarriorSkillSerializer
    queryset = SkillOfWarrior.objects.all()
    lookup_field = 'pk'


class WarriorsSkillsView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorSkillSerializer(warriors, many=True)
        return Response({'Skills': serializer.data})


class WarriorsProfessionsView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorProfessionSerializer(warriors, many=True)
        return Response({'Professions': serializer.data})


class WarriorUpdateView(UpdateAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()
    lookup_field = 'pk'


class WarriorDestroyView(DestroyAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer
