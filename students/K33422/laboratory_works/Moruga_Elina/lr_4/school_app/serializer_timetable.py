from rest_framework import serializers
from .models import Timetable
from .serializer_group import GroupsSerializer
from .serializer_room import RoomSerializer
from .serializer_subject import SubjectSerializer
from .serializer_teacher import TeacherSerializer

class TimetableSerializer(serializers.ModelSerializer):
    room_id = RoomSerializer(read_only=True)
    class_id = GroupsSerializer(read_only=True)
    subject_id = SubjectSerializer(read_only=True)
    teacher_id = TeacherSerializer(read_only=True)
    class Meta:
        model = Timetable
        fields = '__all__'

class TimetableIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = "__all__"

class TimetableCreateSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        timetable = Timetable(**validated_data)
        timetable.save()
        return timetable
    class Meta:
        model = Timetable
        fields = '__all__'
