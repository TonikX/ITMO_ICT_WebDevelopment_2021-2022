from rest_framework import serializers
from .models import *


class WarriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        fields = "__all__"


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ["title", "description"]


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class ProfessionCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()

    def create(self, validated_data):
        profession = Profession(**validated_data)
        profession.save()
        return Profession(**validated_data)



class SkillRelatedSerializer(serializers.ModelSerializer):
    warrior_skills = WarriorSerializer(many=True)

    class Meta:
        model = Skill
        fields = ["title", "warrior_skils"]


class WarriorRelatedSerializer(serializers.ModelSerializer):
    skill = serializers.SlugRelatedField(read_only=True, many=True, slug_field='title')

    # skill = serializers.StringRelatedField(read_only=True, many=True)

    class Meta:
        model = Warrior
        fields = "__all__"

class WarriorProfessionSerializer(serializers.ModelSerializer):
  profession = ProfessionSerializer()

  class Meta:
    model = Warrior
    fields = "__all__"

class WarriorProfessionSkillSerializer(serializers.ModelSerializer):
  profession = ProfessionSerializer()
  skill = serializers.SlugRelatedField(read_only=True, many=True, slug_field='title')

  class Meta:
    model = Warrior
    fields = "__all__"