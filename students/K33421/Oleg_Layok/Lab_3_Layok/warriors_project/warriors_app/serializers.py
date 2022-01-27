from rest_framework import serializers

from .models import *


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = "__all__"


class SkillOfWarriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillOfWarrior
        fields = "__all__"


class WarriorSerializer(serializers.ModelSerializer):
    skills = SkillOfWarriorSerializer(many=True)
    profession = ProfessionSerializer()

    class Meta:
        model = Warrior
        fields = ("race", "name", "level", "profession", "skills")


class WarriorPartialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        fields = ("race", "name", "level", "profession")