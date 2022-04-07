from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import *
from .models import *
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib.auth.validators import UnicodeUsernameValidator


class WorkerSerializer(ModelSerializer):
    class Meta:
        model = Worker
        fields = "__all__"


class ApplicationSerializer(ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class AssignmentSerializer(ModelSerializer):
    class Meta:
        model = Assignment
        fields = "__all__"