from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView, Response
from .serializers import *
from .models import *
from django.db.models.aggregates import Count, Sum


class ExpertAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpertSerializer
    queryset = Expert.objects.all()


class ParticipantAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ParticipantSerializer
    queryset = Participant.objects.all()


class ParticipantRingRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ParticipantRingsSerializer
    queryset = Participant.objects.all()


class ClubBreedsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ClubBreedsSerializer
    queryset = Club.objects.all()


class DismissedCountAPIView(generics.RetrieveAPIView):
    serializer_class = DismissedCountSerializer
    queryset = Show.objects.all()

# leave name
class BreedExpertsAPIView(generics.ListAPIView):
    serializer_class = BreedExpertsSerializer
    queryset = Ring.objects.all()


class BreedCountAPIView(APIView):

    def get(self, request):
        # breed_count = Participant.objects.filter(breed=breed).count()
        breed_count = Participant.objects \
            .values('breed').annotate(count=Count('breed'))
        content = {'breed_count': breed_count}
        return Response(content)


class BreedCountAPIView(APIView):

    def get(self, request):
        # breed_count = Participant.objects.filter(breed=breed).count()
        breed_count = Ring.objects \
            .values('breed').annotate(count=Count('breed'))
        content = {'breed_count': breed_count}
        return Response(content)

# class BreedCountAPIView(generics.ListAPIView):
#     serializer_class = ParticipantSerializer
#     lookup_url_kwarg = "breed"
#
#     def get_queryset(self):
#         breed = self.kwargs.get(self.lookup_url_kwarg)
#         participants = Participant.objects.filter(breed=breed)
#         print(participants)
#         return participants


class ReportAPIView(APIView):

    def get(self, request, year):
        participants = Show.objects.get(year=year).participants
        participant_count = participants.count()
        breed_count = participants.values('breed').annotate(count=Count('breed'))
        best_grades = Grade.objects.filter(ring__show__year=year)\
            .values('participant')\
            .annotate(ex_sum=Sum('final_grade'))\
            .order_by()
        medals = Participant.objects.values('breed')\
            .annotate(medals_count=Count('medals'))
        content = {'participant_count': participant_count,
                   'breeds': breed_count,
                   'best_grades': best_grades,
                   'medals': medals}
        return Response(content)
