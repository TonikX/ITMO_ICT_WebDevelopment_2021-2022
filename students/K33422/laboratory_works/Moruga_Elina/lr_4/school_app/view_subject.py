from rest_framework.views import APIView
from .models import Subject, Timetable
from .serializer_subject import *
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, ListAPIView

class SubjectAPIView(ListAPIView):
    renderer_class = [TemplateHTMLRenderer]
    template_name = 'subject.html'
    serializer_class = SubjectSerializer

    def get_queryset(self):
        queryset = Subject.objects.all()
        params = self.request.query_params 

        subject = params.get("subject", None)
        

        if subject:
            queryset = queryset.filter(subject=subject)

        return queryset