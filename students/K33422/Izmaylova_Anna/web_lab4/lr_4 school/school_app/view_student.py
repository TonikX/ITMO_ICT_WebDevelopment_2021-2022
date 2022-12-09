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
        # получить всех учеников
        queryset = Student.objects.all()
        # из параметров запроса получить пол ученика, по которому будем фильтровать 
        params = self.request.query_params
        gender = params.get("gender", None)

        if gender:
            # отфильтровать учеников по полу
            queryset = queryset.filter(gender=gender)

        # вернуть список учеников
        return queryset


class StudentCreateView(CreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class StudentDelete(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentIDSerializer
