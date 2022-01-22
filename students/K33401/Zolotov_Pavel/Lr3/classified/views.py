from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from classified.serializers import *


class JobApiGetView(APIView):
    def get(self, request):
        jobs = Job.objects.filter(title__icontains=request.GET.get("title", ""))
        serializer = JobSerializer(jobs, many=True)
        return Response({"Jobs": serializer.data})


class JobApiCreateView(CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class IndustryGetView(ListAPIView):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer


class IndustryApiCreateView(CreateAPIView):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer


class RegionGetView(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class RegionApiCreateView(CreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class CompanyGetView(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyApiCreateView(CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class JobResponseGetView(ListAPIView):
    queryset = JobResponse.objects.all()
    serializer_class = JobResponseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return JobResponse.objects.filter(user=user)


class JobResponseApiCreateView(CreateAPIView):
    queryset = JobResponse.objects.all()
    serializer_class = JobResponseSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
