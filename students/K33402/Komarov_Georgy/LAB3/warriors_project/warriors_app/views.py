from drf_spectacular.utils import extend_schema_view
from rest_framework.viewsets import ModelViewSet

from warriors_app.models import Warrior, Profession, Skill
from warriors_app.serializers import ProfessionSerializer, WarriorSerializer, SkillSerializer
from warriors_app.openapi import *


@extend_schema_view(
    create=profession_create_schema,
    retrieve=profession_retrieve_schema,
    list=profession_list_schema,
    update=profession_update_schema,
    partial_update=profession_update_schema,
    destroy=profession_delete_schema,
)
class ProfessionViewSet(ModelViewSet):
    serializer_class = ProfessionSerializer
    queryset = Profession.objects.all()


@extend_schema_view(
    create=skill_create_schema,
    retrieve=skill_retrieve_schema,
    list=skill_list_schema,
    update=skill_update_schema,
    partial_update=skill_update_schema,
    destroy=skill_delete_schema,
)
class SkillViewSet(ModelViewSet):
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()


@extend_schema_view(
    create=warrior_create_schema,
    retrieve=warrior_retrieve_schema,
    list=warrior_list_schema,
    update=warrior_update_schema,
    partial_update=warrior_update_schema,
    destroy=warrior_delete_schema,
)
class WarriorViewSet(ModelViewSet):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()
