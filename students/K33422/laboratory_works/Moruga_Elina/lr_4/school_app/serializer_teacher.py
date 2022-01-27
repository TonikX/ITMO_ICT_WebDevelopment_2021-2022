from rest_framework import serializers
from .models import Teacher
from .serializer_group import GroupsSerializer
from .serializer_room import RoomSerializer

class TeacherSerializer(serializers.ModelSerializer):
    room_id = RoomSerializer(read_only=True)
    group_id = GroupsSerializer(read_only=True)
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'patronymic', 'email', 'id', 'room_id',
        'group_id']
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        teacher = Teacher.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'])
        teacher.set_password(validated_data['password'])
        teacher.save()
        return teacher

class TeacherIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'patronymic', 'email', 'id', 'room_id',
        'group_id']

