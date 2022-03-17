from requests import Response
from rest_framework import generics
from rest_framework.exceptions import APIException
from datetime import datetime
from django.db.models import Count
from .serializers import *


class ClimberCreateAPIView(generics.CreateAPIView):
    serializer_class = ClimberSerializer

class PeakListAPIView(generics.ListAPIView):
    serializer_class = PeakSerializer
    queryset = Peak.objects.all()


class PeakCreateAPIView(generics.CreateAPIView):
    serializer_class = PeakSerializer


class ClimberDetailUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ClimberSerializer
    queryset = Person.objects.all()


class PeakDetailUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = PeakSerializer
    queryset = Peak.objects.all()


class ClimbingCreateAPIView(generics.CreateAPIView):
    serializer_class = ClimbingSerializer


class ParticipationCreateAPIView(generics.CreateAPIView):
    serializer_class = ParticipationSerializer

class EmergencySituationCreateAPIView(generics.CreateAPIView):
    serializer_class = EmergencySituationSerializer

    def perform_create(self, serializer):
        climbing = int(self.request.data['climbing'])
        participant = int(self.request.data['person'])
        if not Participation.objects.filter(climbing_id=climbing, participant_id=participant).count():
            raise APIException('Альпинист не участвовал в восхождении')
        serializer.save()

class EmergencySituationAPIView(generics.ListAPIView):
    serializer_class = EmergencySituationSerializer
    queryset = EmergencySituation.objects.all()


class ClimbingResultForClubCreateAPIView(generics.CreateAPIView):
    serializer_class = ClimbingResultForClubSerializer

    def perform_create(self, serializer):
        climbing = int(self.request.data['climbing'])
        club = int(self.request.data['club'])
        if not Participation.objects.filter(climbing_id=climbing, participant_id=club).count():
            raise APIException('Клуб не участвовал в восхождении')
        serializer.save()


class ClimbingResultForPersonCreateAPIView(generics.CreateAPIView):
    serializer_class = ClimbingResultForPersonSerializer

    def perform_create(self, serializer):
        climbing = int(self.request.data['climbing'])
        participant = int(self.request.data['person'])
        if not Participation.objects.filter(climbing_id=climbing, participant_id=participant).count():
            raise APIException('Альпинист не участвовал в восхождении')
        serializer.save()


class ClimberClimbingListAPIView(generics.ListAPIView):
    serializer_class = ClimberSerializer

    def get_queryset(self):
        if not self.request.query_params:
            return Person.objects.all()
        from_date = [int(i) for i in self.request.query_params.get('from').split('-')]
        from_date = datetime(*from_date)
        to_date = [int(i) for i in self.request.query_params.get('to').split('-')]
        to_date = datetime(*to_date, 23, 59, 59)
        queryset = Person.objects.filter(climbings__start_time__lte=to_date, climbings__finish_time__gte=from_date)
        print(queryset)
        return queryset


class FromToClimbingListAPIView(generics.ListAPIView):
    serializer_class = ClimbingSerializer

    def get_queryset(self):
        if not self.request.query_params:
            return Climbing.objects.all()
        from_date = [int(i) for i in self.request.query_params.get('from').split('-')]
        from_date = datetime(*from_date)
        to_date = [int(i) for i in self.request.query_params.get('to').split('-')]
        to_date = datetime(*to_date, 23, 59, 59)
        queryset = Climbing.objects.filter(start_time__lte=to_date, finish_time__gte=from_date)
        print(queryset)
        return queryset


class ClimbersOnPeakListAPIView(generics.ListAPIView):
    serializer_class = ClimberSerializer

    def get_queryset(self):
        pk = int(self.kwargs['pk'])
        queryset = Person.objects.filter(climbing__peak_id=pk).distinct()
        return queryset


class PeakWithoutClimbingListAPIView(generics.ListAPIView):
    serializer_class = PeakSerializer

    def get_queryset(self):
        queryset = Peak.objects.annotate(num_climbings=Count('climbing')).filter(num_climbings=0)
        print(queryset)
        return queryset


class CountClimbersOnPeakListAPIView(generics.ListAPIView):
    serializer_class = CountClimbersSerializer

    def get_queryset(self):
        pk = int(self.kwargs['pk'])
        queryset = Person.objects.filter(climbing__peak_id=pk).annotate(climbings_on_peak=Count('climbing'))
        return queryset
