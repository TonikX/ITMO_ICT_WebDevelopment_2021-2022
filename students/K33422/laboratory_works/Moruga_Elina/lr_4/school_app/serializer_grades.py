from rest_framework import serializers
from .models import Grades
from .serializer_student import StudentSerializer
from .serializer_subject import SubjectSerializer

class GradesSerializer(serializers.ModelSerializer):
    student_id = StudentSerializer(read_only=True)
    subject_id = SubjectSerializer(read_only=True)
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