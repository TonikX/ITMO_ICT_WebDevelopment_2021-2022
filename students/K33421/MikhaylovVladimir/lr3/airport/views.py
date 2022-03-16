from django.shortcuts import render, get_object_or_404
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from airport.models import *
from airport.serializers import *


# Работник

class WorkerAPIView(generics.ListCreateAPIView):
    serializer_class = WorkerViewSerializer
    queryset = Worker.objects.all()


class WorkerCreateAPIView(generics.ListCreateAPIView):
    serializer_class = WorkerCreateSerializer
    queryset = Worker.objects.all()


class WorkerRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerViewSerializer


# Самолёт

class PlaneListAPIView(generics.ListAPIView):
    serializer_class = PlaneViewSerializer

    def get_queryset(self):
        queryset = Plane.objects.all()
        params = self.request.query_params

        type = params.get('type', None)
        number = params.get('number', None)
        mesta = params.get('mesta', None)
        speed = params.get('speed', None)
        avia = params.get('avia', None)

        if type:
            queryset = queryset.filter(type=type)

        if number:
            queryset = queryset.filter(number=number)

        if mesta:
            queryset = queryset.filter(mesta=mesta)

        if speed:
            queryset = queryset.filter(speed=speed)

        if avia:
            queryset = queryset.filter(avia=avia)
        return queryset


class PlaneCreateAPIView(generics.CreateAPIView):
    queryset = Plane.objects.all()
    serializer_class = PlaneCreateSerializer


class PlaneRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plane.objects.all()
    serializer_class = PlaneViewSerializer


# Ремонт

class RemontCreateAPIView(generics.ListCreateAPIView):
    serializer_class = RemontViewSerializer
    queryset = Remont.objects.all()


class RemontDepthAPIView(APIView):
    def get(self, request):
        remont = Remont.objects.all()
        serializer = RemontDepthSerializer(remont, many=True)
        return Response({"Remont": serializer.data})


class RemontListAPIView(generics.ListAPIView):
    serializer_class = RemontViewSerializer
    queryset = Remont.objects.all()


class RemontRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Remont.objects.all()
    serializer_class = RemontViewSerializer


# Экипаж

class EkipazhListAPIView(generics.ListAPIView):
    serializer_class = EkipazhViewSerializer

    def get_queryset(self):
        queryset = Ekipazh.objects.all()
        params = self.request.query_params

        name = params.get('name', None)

        if name:
            queryset = queryset.filter(type=name)
        return queryset


class EkipazhCreateAPIView(generics.CreateAPIView):
    queryset = Ekipazh.objects.all()
    serializer_class = EkipazhViewSerializer


class EkipazhRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ekipazh.objects.all()
    serializer_class = EkipazhViewSerializer


# Штаб авиакомпании

class AviacompanyListAPIView(generics.ListAPIView):
    queryset = Aviacompany.objects.all()
    serializer_class = AviacompanyNestedSerializer


class AviacompanyCreateAPIView(generics.CreateAPIView):
    queryset = Aviacompany.objects.all()
    serializer_class = AviacompanyCreateSerializer


class AviacompanyRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aviacompany.objects.all()
    serializer_class = AviacompanyViewSerializer


# Транзит
class TranzitListAPIView(generics.ListAPIView):
    queryset = Tranzit.objects.all()
    serializer_class = TranzitViewSerializer


class TranzitCreateAPIView(generics.CreateAPIView):
    queryset = Tranzit.objects.all()
    serializer_class = TranzitViewSerializer


class TranzitRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tranzit.objects.all()
    serializer_class = TranzitViewSerializer


# Разрешение для пилотирования самолётом
class RazrechenieListAPIView(generics.ListAPIView):
    queryset = Razrechenie.objects.all()
    serializer_class = RazrechenieNestedSerializer


class RazrechenieCreateAPIView(generics.CreateAPIView):
    queryset = Razrechenie.objects.all()
    serializer_class = RazrechenieCreateSerializer


class RazrechenieRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Razrechenie.objects.all()
    serializer_class = RazrechenieViewSerializer


# Рейс
class ReysListAPIView(generics.ListAPIView):
    queryset = Reys.objects.all()
    serializer_class = ReysViewSerializer


class ReysCreateAPIView(generics.CreateAPIView):
    queryset = Reys.objects.all()
    serializer_class = ReysViewSerializer


class ReysRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reys.objects.all()
    serializer_class = ReysViewSerializer


# Допуск к полёту
class DopuskListAPIView(generics.ListAPIView):
    queryset = Dopusk.objects.all()
    serializer_class = DopuskNestedSerializer


class DopuskCreateAPIView(generics.CreateAPIView):
    queryset = Dopusk.objects.all()
    serializer_class = DopuskCreateSerializer


class DopuskRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dopusk.objects.all()
    serializer_class = DopuskViewSerializer


# Полёт
class PoletDetailListAPIView(generics.ListAPIView):
    queryset = Polet.objects.all()
    serializer_class = PoletNestedSerializer


class PoletCreateAPIView(generics.CreateAPIView):
    queryset = Polet.objects.all()
    serializer_class = PoletViewSerializer


class PoletRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Polet.objects.all()
    serializer_class = PoletViewSerializer


class PoletListAPIView(generics.ListAPIView):
    queryset = Polet.objects.all()
    serializer_class = PoletViewSerializer