from rest_framework.views import APIView
from .models import Grades
from .serializer_grades import *
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView

class GradesAPIView(APIView):
    def get(self, request):
        grades = Grades.objects.all()
        serializer = GradesSerializer(grades, many=True)
        return Response({"Grades": serializer.data})

class GradesCreateView(CreateAPIView):
    serializer_class = GradesSerializer
    queryset =  Grades.objects.all()

class GradesUpdate(UpdateAPIView):
    queryset = Grades.objects.all()
    serializer_class = GradesIDSerializer