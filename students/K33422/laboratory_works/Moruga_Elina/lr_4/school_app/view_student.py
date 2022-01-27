from rest_framework.views import APIView
from .models import Student
from .serializer_student import *
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, ListAPIView

class StudentAPIView(ListAPIView):
    renderer_class = [TemplateHTMLRenderer]
    template_name = 'students_list.html'
    serializer_class = StudentSerializer
    def get_queryset(self):
        queryset = Student.objects.all()
        params = self.request.query_params 

        gender = params.get("gender", None)
        
        if gender:
            queryset = queryset.filter(gender=gender)

        return queryset


class StudentCreateView(CreateAPIView):
    serializer_class = StudentSerializer
    queryset =  Student.objects.all()

class StudentDelete(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentIDSerializer

class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentIDSerializer 