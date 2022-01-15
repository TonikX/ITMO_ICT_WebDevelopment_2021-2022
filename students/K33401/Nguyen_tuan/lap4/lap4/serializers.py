from rest_framework import serializers
from lap4.models import *
class historybillSerializer(serializers.ModelSerializer):
    class Meta:
        model=historybill
        fields = "__all__"
