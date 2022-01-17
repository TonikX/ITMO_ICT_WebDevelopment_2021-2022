from rest_framework import serializers
from .models import *


class WarriorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Warrior
        fields = "__all__"

    def create(self, validated_data):
        warrior = Warrior(**validated_data)
        warrior.save()
        return Warrior(**validated_data)

class ProfessionCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()
    class Meta:
        model = Profession
        fields = "__all__"

        def create(self, validated_data):
            profession = Profession(**validated_data)
            profession.save()
            return Profession(**validated_data)

class SkillCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"

        def create(self, validated_data):
            skill = Skill(**validated_data)
            skill.save()
            return Skill(**validated_data)

class WarriorSkillSerializer(serializers.ModelSerializer):
    skill = SkillCreateSerializer(many=True)
    #skill = serializers.SlugRelatedField(read_only=True, many=True, slug_field='title')
    class Meta:
        model = Warrior
        fields = "__all__"

class WarriorProfessionSerializer(serializers.ModelSerializer):
    profession = ProfessionCreateSerializer()
    class Meta:
        model = Warrior
        fields = "__all__"

class WarriorIDSerializer(serializers.ModelSerializer):
    profession = ProfessionCreateSerializer()
    skill = SkillCreateSerializer(many=True)
    class Meta:
        model = Warrior
        fields = "__all__"