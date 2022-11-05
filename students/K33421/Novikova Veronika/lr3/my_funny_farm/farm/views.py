from django.shortcuts import render
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ChickenListAPIView(generics.ListAPIView):
    serializer_class = AllChickenRelatedSerializer
    queryset = Chicken.objects.all()


class ChickenInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chicken.objects.all()
    serializer_class = ChickenSerializer


class ChickenCreateAPIView(generics.CreateAPIView):
    serializer_class = ChickenSerializer
    queryset = Chicken.objects.all()


class BreedListAPIView(generics.ListAPIView):
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()


class BreedInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class BreedCreateAPIView(generics.CreateAPIView):
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()


class WorkListAPIView(generics.ListAPIView):
    serializer_class = WorkRelatedSerializer
    queryset = Working.objects.all()


class WorkInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Working.objects.all()
    serializer_class = WorkSerializer


class WorkCreateAPIView(generics.CreateAPIView):
    serializer_class = WorkSerializer
    queryset = Working.objects.all()


class CageListAPIView(generics.ListAPIView):
    serializer_class = CageSerializer
    queryset = Cage.objects.all()


class CageInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cage.objects.all()
    serializer_class = CageSerializer


class CageCreateAPIView(generics.CreateAPIView):
    serializer_class = CageSerializer
    queryset = Cage.objects.all()


