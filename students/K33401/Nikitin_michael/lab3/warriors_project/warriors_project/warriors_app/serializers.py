from django.db.models import fields
from rest_framework import serializers
from .models import Warrior, Skill, Profession


class SkillSerializer(serializers.ModelSerializer):

   class Meta:
      model = Skill
      fields = "__all__"

class ProfessionSerializer(serializers.ModelSerializer):

   class Meta:
      model = Profession
      fields = "__all__"


class ProfessionCreateSerializer(serializers.Serializer):
   title = serializers.CharField(max_length=120)
   description = serializers.CharField()

   def create(self, validated_data):
      profession = Profession(**validated_data)
      profession.save()
      return profession


class SkillCreateSerializer(serializers.Serializer):
   title = serializers.CharField(max_length=120)   

   def create(self, validated_data):
      skill = Skill(**validated_data)
      skill.save()
      return skill


class WarriorSerializer(serializers.ModelSerializer):

  class Meta:
     model = Warrior
     fields = "__all__"


class WarriorDetailSerializer(serializers.ModelSerializer):
   # наследование
   profession = ProfessionSerializer()
   skill = SkillSerializer(many=True)

   # уточнение поля
   race = serializers.CharField(source="get_race_display", read_only=True)

   class Meta:
      model = Warrior
      fields = "__all__"


class WarriorProfessionSerializer(serializers.ModelSerializer):
   profession = ProfessionSerializer()

   class Meta:
      model = Warrior
      fields = "__all__"

class WarriorSkillSerializer(serializers.ModelSerializer):
   skill = SkillSerializer(many=True)

   class Meta:
      model = Warrior
      fields = "__all__"
