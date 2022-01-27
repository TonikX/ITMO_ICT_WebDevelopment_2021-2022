from rest_framework.serializers import ModelSerializer

from .models import *


class WarriorSkillSerializer(ModelSerializer):
    class Meta:
        model = SkillOfWarrior
        fields = '__all__'


class ProfessionSerializer(ModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__'


class WarriorSerializer(ModelSerializer):
    class Meta:
        model = Warrior
        fields = '__all__'

    skill = WarriorSkillSerializer(source='skillofwarrior_set', many=True, read_only=True)


class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class WarriorProfessionSerializer(ModelSerializer):
    profession = ProfessionSerializer()

    class Meta:
        model = Warrior
        fields = '__all__'


class SingleWarriorSerializer(ModelSerializer):
    class Meta:
        model = Warrior
        read_only_fields = ['id']
        fields = '__all__'
        depth = 1

    profession = ProfessionSerializer()
    skill = WarriorSkillSerializer(source='skillofwarrior_set', many=True, read_only=True)
