from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Subject, Timetable, Room, Groups
from .serializer_room import *
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, ListAPIView


class RoomAPIView(ListAPIView):
    renderer_class = [TemplateHTMLRenderer]
    template_name = 'room.html'
    serializer_class = RoomSerializer

    def get_queryset(self):
        queryset = Subject.objects.all()
        params = self.request.query_params

        status = params.get("status", None)

        if status:
            subjects = queryset.filter(status=status).values('id')
            subjects = [item["id"] for item in list(subjects)]
            print(subjects)
            rooms = Timetable.objects.all().filter(subject_id__in=subjects).values('room_id')
            rooms = [item["room_id"] for item in list(rooms)]
            print(rooms)
            return Room.objects.all().filter(id__in=rooms)

        return Room.objects.all()


class ClassViewSet(ModelViewSet):
    queryset = Groups.objects.all()
    serializer_class = GroupSerializer
