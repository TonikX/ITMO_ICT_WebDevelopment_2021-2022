from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import City, Favourite
from .serializers import *

# Create your views here.

class UserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = User.objects.filter(id=request.user.id)
        serializer = UserSerializer(user, many=True)
        return Response({"Users": serializer.data})


class CityAPIView(APIView):

    def get(self, request):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response({"Cities": serializer.data})


class CityCreateView(APIView):

    def post(self, request):
        city = request.data.get("city")
        serializer = CityCreateSerializer(data=city)

        if serializer.is_valid(raise_exception=True):
            city_saved = serializer.save()

        return Response({"Success": "City '{}' created succesfully.".format(city_saved.name)})


class FavouriteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        favourites = Favourite.objects.all()
        serializer = FavouriteSerializer(favourites, many=True)
        return Response({"Favourites": serializer.data})


class FavouriteCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        favourite = request.data.get("Favourite")
        serializer = FavouriteCreateSerializer(data=favourite)

        if serializer.is_valid(raise_exception=True):
            favourite_saved = serializer.save()

        return Response({"Success": "Favourite '{}' created succesfully.".format(favourite_saved.id)})


class FavouriteDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user_id = request.GET.get('user_id')
        city_id = request.GET.get('city_id')

        favourite = Favourite.objects.get(user_id=user_id, city_id=city_id)
        favourite.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
