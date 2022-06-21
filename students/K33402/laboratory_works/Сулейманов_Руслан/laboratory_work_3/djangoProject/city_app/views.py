from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from city_app.models import CityList
from city_app.serializers import CitySerializer


class CityView(APIView):
    def get(self, request):
        name = self.request.query_params.get('name')
        if name:
            cities = CityList.objects.filter(name__istartswith=name)[:20]
        else:
            cities = CityList.objects.all()[:20]
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)
