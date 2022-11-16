from django.urls import path
from .views import *

urlpatterns = [
    path('climbers/', ClimberClimbingListAPIView.as_view()),
    path('climbers/create', ClimberCreateAPIView.as_view()),
    path('climbers/<int:pk>', ClimberDetailUpdateAPIView.as_view()),
    path('peaks/', PeakListAPIView.as_view()),
    path('peaks/create', PeakCreateAPIView.as_view()),
    path('peaks/<int:pk>', PeakDetailUpdateAPIView.as_view()),
    path('peaks/<int:pk>/unique_climbers', ClimbersOnPeakListAPIView.as_view()),
    path('peaks/no_trips', PeakWithoutClimbingListAPIView.as_view()),
    path('peaks/<int:pk>/climbers', CountClimbersOnPeakListAPIView.as_view()),
    path('trip/', FromToClimbingListAPIView.as_view()),
    path('trip/create', ClimbingCreateAPIView.as_view()),
    path('trip/<int:pk>/result_for_club', ClimbingResultForClubCreateAPIView.as_view()),
    path('trip/<int:pk>/result_for_person', ClimbingResultForPersonCreateAPIView.as_view()),
    path('members/create', ParticipationCreateAPIView.as_view()),
    path('emergencies/', EmergencySituationAPIView.as_view()),
    path('emergencies/create', EmergencySituationCreateAPIView.as_view()),
]