from rest_framework.viewsets import ModelViewSet

from warriors_app.models import Warrior, Profession, Skill
from warriors_app.serializers import ProfessionSerializer, WarriorSerializer, SkillSerializer


class ProfessionViewSet(ModelViewSet):
    serializer_class = ProfessionSerializer
    queryset = Profession.objects.all()


class SkillViewSet(ModelViewSet):
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()


class WarriorViewSet(ModelViewSet):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()
