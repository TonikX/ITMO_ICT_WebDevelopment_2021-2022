from django.urls import path
from .views import *

app_name = "airport"

urlpatterns = [
    path('workers/', WorkerAPIView.as_view()),
    path('worker/create/', WorkerCreateAPIView.as_view()),
    path('worker/<int:pk>/', WorkerRUDAPIView.as_view()),

    path('planes/', PlaneListAPIView.as_view()),
    path('plane/create/', PlaneCreateAPIView.as_view()),
    path('plane/<int:pk>/', PlaneRUDAPIView.as_view()),

    path('remont/create/', RemontCreateAPIView.as_view()),
    path('remont/depth/', RemontDepthAPIView.as_view()),
    path('remont/', RemontListAPIView.as_view()),
    path('remont/<int:pk>/', RemontRUDAPIView.as_view()),

    path('ekipazh/', EkipazhListAPIView.as_view()),
    path('ekipazh/create/', EkipazhCreateAPIView.as_view()),
    path('ekipazh/<int:pk>/', EkipazhRUDAPIView.as_view()),

    path('aviacompany/', AviacompanyListAPIView.as_view()),
    path('aviacompany/<int:pk>/', AviacompanyRUDAPIView.as_view()),
    path('aviacompany/create/', AviacompanyCreateAPIView.as_view()),

    path('tranzit/', TranzitListAPIView.as_view()),
    path('tranzit/create/', TranzitCreateAPIView.as_view()),
    path('tranzit/<int:pk>/', TranzitRUDAPIView.as_view()),

    path('razrechenie/', RazrechenieListAPIView.as_view()),
    path('razrechenie/create/', RazrechenieCreateAPIView.as_view()),
    path('razrechenie/<int:pk>/', RazrechenieRUDAPIView.as_view()),

    path('reys/', ReysListAPIView.as_view()),
    path('reys/create/', ReysCreateAPIView.as_view()),
    path('reys/<int:pk>/', ReysRUDAPIView.as_view()),

    path('dopusk/', DopuskListAPIView.as_view()),
    path('dopusk/create/', DopuskCreateAPIView.as_view()),
    path('dopusk/<int:pk>/', DopuskRUDAPIView.as_view()),

    path('polet/', PoletListAPIView.as_view()),
    path('polet/detail/', PoletDetailListAPIView.as_view()),
    path('polet/create/', PoletCreateAPIView.as_view()),
    path('polet/<int:pk>/', PoletRUDAPIView.as_view())
]