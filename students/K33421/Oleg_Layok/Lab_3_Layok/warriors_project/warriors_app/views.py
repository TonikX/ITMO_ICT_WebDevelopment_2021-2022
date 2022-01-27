from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from warriors_app.models import Warrior, Skill, Profession, SkillOfWarrior
from warriors_app.serializers import WarriorSerializer, SkillSerializer, ProfessionSerializer, WarriorPartialSerializer,\
    SkillOfWarriorSerializer


class WarriorAPIView(viewsets.ModelViewSet):
    queryset = Warrior.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return WarriorSerializer
        return WarriorPartialSerializer


class SkillAPIView(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response({"Skills": serializer.data})

    def post(self, request):
        serializer = SkillSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            skill_saved = serializer.save()
            return Response({"Success": "skill '{}' created successfully.".format(skill_saved.title)})


class ProfessionCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProfessionSerializer
    queryset = Profession.objects.all()


class SkillOfWarriorAPIView(viewsets.ModelViewSet):
    serializer_class = SkillOfWarriorSerializer
    queryset = SkillOfWarrior.objects.all()