from django.db.models import fields
from rest_framework import serializers
from .models import *

# Warriors
class WarriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        fields = "__all__"

class WarriorSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        fields = ["name", "skills"]

class WarriorProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        fields = ["name", "profession"]

#  Profession
class ProfessionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = "__all__"

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"

class SkillCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"

class WarriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        fields = "__all__"