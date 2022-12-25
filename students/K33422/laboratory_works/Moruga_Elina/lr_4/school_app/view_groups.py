from rest_framework.views import APIView
from .models import Groups
from .serializer_group import *
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, ListAPIView

class GroupsAPIView(ListAPIView):
    serializer_class = GroupsSerializer

    def get_queryset(self):
        return Groups.objects.all()