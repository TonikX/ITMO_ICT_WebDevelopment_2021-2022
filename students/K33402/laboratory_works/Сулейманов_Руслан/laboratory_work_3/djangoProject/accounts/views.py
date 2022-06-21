from rest_framework.viewsets import  GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin,RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Membership
from accounts.serializers import UserSerializer, CityUserSerializer


class UserViewAPI(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class UserCitytDetail(DestroyModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Membership.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CityUserSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserCitytList(CreateModelMixin, ListModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CityUserSerializer

    def get_queryset(self):
        return Membership.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)