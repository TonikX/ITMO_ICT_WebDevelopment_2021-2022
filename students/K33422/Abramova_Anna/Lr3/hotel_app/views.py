from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from hotel_app.models import Admin, Room, Client, Inhabitation, Cleaner, Cleaning
from hotel_app.serializers import AdminSerializer, RoomSerializer, ClientSerializer, InhabitationSerializer, \
    CleanerSerializer, CleaningSerializer


class AdminViewSet(ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [IsAdminUser]


class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [SearchFilter]
    search_fields = ['full_name']


class InhabitationViewSet(ModelViewSet):
    queryset = Inhabitation.objects.all()
    serializer_class = InhabitationSerializer
    permission_classes = [IsAuthenticated]


class CleanerViewSet(ModelViewSet):
    queryset = Cleaner.objects.all()
    serializer_class = CleanerSerializer
    permission_classes = [IsAuthenticated]


class CleaningViewSet(ModelViewSet):
    queryset = Cleaning.objects.all()
    serializer_class = CleaningSerializer
    permission_classes = [IsAuthenticated]

