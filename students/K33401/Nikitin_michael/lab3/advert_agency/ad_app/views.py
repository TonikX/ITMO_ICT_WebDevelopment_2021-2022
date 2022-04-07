from .serializers import *
from rest_framework.generics import *
from .models import *
from rest_framework.permissions import *
from rest_framework.status import *
from rest_framework.views import APIView
from rest_framework.response import Response


class IsApplicationOwner(BasePermission):
    message = 'You are not allowed to change this application'

    def has_object_permission(self, request, view, obj):
        return obj.worker.user == request.user or obj.client.user == request.user


class IsAssignmentOwner(BasePermission):
    message = 'You are not allowed to see this assignment'

    def has_object_permission(self, request, view, obj):
        return obj.application.worker.user == request.user


class WorkersAPI(ListAPIView):
    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()


class ServiceCreateAPI(CreateAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()


class ServiceUpdateAPI(UpdateAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

    lookup_field = 'pk'


class ServiceAPI(ListAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()


class ServiceDeleteAPI(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

    lookup_field = 'pk'


class ServiceDetailsAPI(RetrieveAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

    lookup_field = 'pk'


class ApplicationsAPI(ListAPIView):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()


class ApplicationsCreateAPI(CreateAPIView):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()


class ApplicationsDeleteAPI(DestroyAPIView):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()

    lookup_field = 'pk'


class ApplicationsUpdateAPI(UpdateAPIView):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()
    permission_classes = [IsAuthenticated, IsApplicationOwner]

    lookup_field = 'pk'


class ApplicationsDetailsAPI(RetrieveAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated, IsApplicationOwner]

    lookup_field = 'pk'


class AssignmentAPI(ListAPIView):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()


class AssignmentCreateAPI(CreateAPIView):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()


class AssignmentDeleteAPI(DestroyAPIView):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()

    lookup_field = 'pk'


class AssignmentUpdateAPI(UpdateAPIView):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()
    permission_classes = [IsAuthenticated, IsAssignmentOwner]

    lookup_field = 'pk'


class AssignmentDetailsAPI(RetrieveAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated, IsAssignmentOwner]

    lookup_field = 'pk'
