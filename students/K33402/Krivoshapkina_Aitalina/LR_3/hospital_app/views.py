from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics
from .models import *


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = "__all__"


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"


class ScheduleOfDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleOfDoctor
        fields = "__all__"


class CabinetOfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CabinetOfficer
        fields = "__all__"


class CabinetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cabinet
        fields = "__all__"


class ScheduleOfCabinetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleOfCabinet
        fields = "__all__"


class PriceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceList
        fields = "__all__"


class VisitSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()
    patient = PatientSerializer()
    cabinet = CabinetSerializer()
    price = PriceListSerializer()
    class Meta:
        model = Visit
        fields = "__all__"


class VisitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = "__all__"

    def validate(self, data):
        if data['doctor'].date_of_start > data['date'] and (data['doctor'].date_of_end is None or data['doctor'].date_of_end < data['date']):
            raise serializers.ValidationError("Выберите другого доктора или дату")

        weekdays_of_doctor = []
        schedule_of_doctors = ScheduleOfDoctor.objects.filter(doctor=data['doctor'])
        for item in schedule_of_doctors:
            weekdays_of_doctor.append(item.weekday)
        weekday = weekdays[data['date'].weekday()][0]

        if weekday not in weekdays_of_doctor:
            raise serializers.ValidationError("В этот день недели доктор не работает")

        return data


class MedicalCardSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    visit = VisitSerializer()

    class Meta:
        model = MedicalCard
        fields = "__all__"


class MedicalCardCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalCard
        fields = "__all__"


class PatientAPIView(viewsets.ModelViewSet):
   serializer_class = PatientSerializer
   queryset = Patient.objects.all()


class SpecializationAPIView(viewsets.ModelViewSet):
   serializer_class = SpecializationSerializer
   queryset = Specialization.objects.all()


class DoctorAPIView(viewsets.ModelViewSet):
   serializer_class = DoctorSerializer
   queryset = Doctor.objects.all()


class ScheduleOfDoctorAPIView(viewsets.ModelViewSet):
   serializer_class = ScheduleOfDoctorSerializer
   queryset = ScheduleOfDoctor.objects.all()


class CabinetAPIView(viewsets.ModelViewSet):
   serializer_class = CabinetSerializer
   queryset = Cabinet.objects.all()


class ScheduleOfCabinetAPIView(viewsets.ModelViewSet):
   serializer_class = ScheduleOfCabinetSerializer
   queryset = ScheduleOfCabinet.objects.all()


class PriceListAPIView(viewsets.ModelViewSet):
   serializer_class = PriceListSerializer
   queryset = PriceList.objects.all()


class VisitAPIView(viewsets.ModelViewSet):
   serializer_class = VisitSerializer
   queryset = Visit.objects.all()

   def get_serializer_class(self):
       if self.action == 'create':
           return VisitCreateSerializer
       else:
           return VisitSerializer


class MedicalCardAPIView(viewsets.ModelViewSet):
   serializer_class = MedicalCardSerializer
   queryset = MedicalCard.objects.all()

   def get_serializer_class(self):
       if self.action == 'create':
           return MedicalCardCreateSerializer
       else:
           return MedicalCardSerializer


class CabinetOfficerAPIView(viewsets.ModelViewSet):
   serializer_class = CabinetOfficerSerializer
   queryset = CabinetOfficer.objects.all()
