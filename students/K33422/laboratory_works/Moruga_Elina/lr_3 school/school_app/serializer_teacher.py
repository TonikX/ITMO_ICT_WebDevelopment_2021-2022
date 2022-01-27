from rest_framework import serializers
from .models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['username', 'password', 'first_name', 'last_name',
                'patronymic', 'email']
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
        fields = ['username', 'first_name', 'last_name',
                'patronymic', 'email', 'room_id', 'group_id', 'id']

