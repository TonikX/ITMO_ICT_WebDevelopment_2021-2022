from rest_framework.views import APIView
from .models import Timetable
from .serializer_timetable import *
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, ListAPIView

class TimetableAPIView(ListAPIView):
    renderer_class = [TemplateHTMLRenderer]
    template_name = 'timetable.html'
    serializer_class = TimetableSerializer

    def get_queryset(self):
        queryset = Timetable.objects.all()
        params = self.request.query_params 

        subject = params.get("subject_id", None)
        day = params.get("day", None)
        lesson = params.get("lesson", None)

        if subject and day and lesson:
            queryset = queryset.filter(subject_id=subject)
            queryset = queryset.filter(day_of_week=day)
            queryset = queryset.filter(lesson=lesson)

        return queryset

class TimetableCreateView(CreateAPIView):
    serializer_class = TimetableSerializer
    queryset =  Timetable.objects.all()

class TimetableUpdate(UpdateAPIView):
    queryset = Timetable.objects.all()
    serializer_class = TimetableIDSerializer