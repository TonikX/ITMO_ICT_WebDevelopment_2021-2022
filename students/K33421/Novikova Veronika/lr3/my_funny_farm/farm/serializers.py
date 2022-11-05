from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'passport', 'cage']


class ChickenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chicken
        fields = "__all__"


class AllChickenRelatedSerializer(serializers.ModelSerializer):
    breed = serializers.StringRelatedField(read_only=True)
    cage = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Chicken
        fields = "__all__"


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = "__all__"


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Working
        fields = "__all__"


class WorkRelatedSerializer(serializers.ModelSerializer):
    username = serializers.StringRelatedField(read_only=True)
    cage = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Working
        fields = "__all__"


class CageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cage
        fields = "__all__"


