from rest_framework.generics import CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from warriors_app.models import Warrior, Skill
from warriors_app.serializers import WarriorSerializer, ProfessionSerializer, SkillSerializer, \
    WarriorProfessionSerializer, WarriorSkillsSerializer, WarriorProfessionsSkillsSerializer


class WarriorAPIView(APIView):
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


class SkillsView(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response({"skills": serializer.data})


class SkillsCreateView(APIView):
    def post(self, request):
        skill = request.data.get("skill")
        serializer = SkillSerializer(data=skill)

        if serializer.is_valid(raise_exception=True):
            skill_saved = serializer.save()

        return Response({"Success": "Skill '{}' created successfully.".format(skill_saved.title)})


class WarriorProfessionView(APIView):
    """
    Вывод полной информации о всех войнах и их профессиях (в одном запросе).
    """
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorProfessionSerializer(warriors, many=True)
        return Response({"warriors": serializer.data})


class WarriorsSkillsView(APIView):
    """
    Вывод полной информации о всех войнах и их скиллах (в одном запросе)
    """
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorSkillsSerializer(warriors, many=True)
        return Response({"warriors": serializer.data})


class WarriorInfoView(RetrieveAPIView):
    """
    Вывод полной информации о войне (по id), его профессиях и скилах.
    """
    queryset = Warrior.objects.all()
    serializer_class = WarriorProfessionsSkillsSerializer


class WarriorDeleteView(DestroyAPIView):
    """
    Удаление война по id.
    """
    queryset = Warrior.objects.all()


class WarriorEditView(UpdateAPIView):
    """
    Редактирование информации о воине
    """
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": f"warrior {instance} updated successfully"})

        else:
            return Response({"message": "failed", "details": serializer.errors})
