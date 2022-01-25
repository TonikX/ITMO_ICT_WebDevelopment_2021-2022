from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        student = Student(**validated_data)
        student.save()
        return student


class StudentIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
