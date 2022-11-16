from rest_framework import serializers

from .models import *


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class SkillOfWarriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillOfWarrior
        fields = ['title', 'level']
        read_only_fields = fields

    title = serializers.CharField(source='skill', read_only=True)


class WarriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        fields = '__all__'

    profession = serializers.SlugRelatedField(slug_field='title', queryset=Profession.objects.all())
    skills = SkillOfWarriorSerializer(source='skillofwarrior_set', many=True, read_only=True)
