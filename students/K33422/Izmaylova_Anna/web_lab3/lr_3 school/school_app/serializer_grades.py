from rest_framework import serializers
from .models import Grades

class GradesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grades
        fields = '__all__'

    def create(self, validated_data):
        grades = Grades(**validated_data)
        grades.save()
        return grades

class GradesIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grades
        fields = "__all__"