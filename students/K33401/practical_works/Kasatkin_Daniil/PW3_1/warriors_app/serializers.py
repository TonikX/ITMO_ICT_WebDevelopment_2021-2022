from rest_framework import serializers
from .models import *


class WarriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        fields = "__all__"


class WarriorDepthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        fields = "__all__"
        depth = 1


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ["title", "description"]


class SkillCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)

    def create(self, validated_data):
        return Skill.objects.create(**validated_data)


class WarriorSkillsNestedSerializer(serializers.ModelSerializer):
    # делаем наследование
    skill = SkillSerializer(many=True)

    # уточняем поле

    class Meta:
        model = Warrior
        fields = "__all__"


class WarriorProfessionsNestedSerializer(serializers.ModelSerializer):
    # делаем наследование
    profession = ProfessionSerializer()

    # уточняем поле

    class Meta:
        model = Warrior
        fields = "__all__"
