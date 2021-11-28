from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import *
from rest_framework.permissions import *
from .serializers import *


class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.type == 'manager'


class IsDeputy(BasePermission):
    def has_permission(self, request, view):
        print(request.user.type)
        return request.user.type == 'deputy'


class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]


class StudentAllView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsDeputy]


class StudentCreateView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsDeputy]


class TeacherListView(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [AllowAny]


class TeacherAllView(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsDeputy]


class TeacherCreateView(CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsDeputy]


class SubjectListView(ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [AllowAny]


class SubjectAllView(RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsDeputy]


class SubjectCreateView(CreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsDeputy]


class MarkListView(ListAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
    permission_classes = [AllowAny]


class MarkAllView(RetrieveUpdateDestroyAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
    permission_classes = [IsDeputy]


class MarkCreateView(CreateAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
    permission_classes = [IsDeputy]


class PairListView(ListAPIView):
    queryset = Pair.objects.all()
    serializer_class = PairSerializer
    permission_classes = [AllowAny]


class PairAllView(RetrieveUpdateDestroyAPIView):
    queryset = Pair.objects.all()
    serializer_class = PairSerializer
    permission_classes = [IsManager]


class PairCreateView(CreateAPIView):
    queryset = Pair.objects.all()
    serializer_class = PairSerializer
    permission_classes = [IsManager]


class SubjectToTeacherListView(ListAPIView):
    queryset = SubjectToTeacher.objects.all()
    serializer_class = SubjectToTeacherSerializer
    permission_classes = [AllowAny]


class SubjectToTeacherAllView(RetrieveUpdateDestroyAPIView):
    queryset = SubjectToTeacher.objects.all()
    serializer_class = SubjectToTeacherSerializer
    permission_classes = [IsDeputy]


class SubjectToTeacherCreateView(CreateAPIView):
    queryset = SubjectToTeacher.objects.all()
    serializer_class = SubjectToTeacherSerializer
    permission_classes = [IsDeputy]
