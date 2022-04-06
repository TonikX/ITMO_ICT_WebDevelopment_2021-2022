from django.http import JsonResponse
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from weather.models import User, Town
from weather.serializers import UserSerializer, TownSerializer


class CreateUserAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class GetUserInfoAPIView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UpdateUserAPIView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CreateTownAPIView(CreateAPIView):
    serializer_class = TownSerializer
    queryset = Town.objects.all()


class GetTownsAPIView(RetrieveAPIView):
    def get(self, request, **kwargs):
        towns = Town.objects.all()
        serializer = TownSerializer(towns, many=True)
        return JsonResponse({'towns': serializer.data})
