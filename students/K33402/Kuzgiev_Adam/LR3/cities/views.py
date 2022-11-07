from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from cities.models import ChosenCity


class ChosenCityView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, city_id):
        if ChosenCity.objects.filter(user=self.request.user).filter(city_id=city_id).exists():
            return Response({'detail': 'Нелья выбрать один город дважды'}, status=400)
        ChosenCity.objects.create(user=self.request.user, city_id=city_id)
        return Response(status=201)

    def delete(self, request, city_id):
        if not ChosenCity.objects.filter(user=self.request.user.id).filter(city_id=city_id).exists():
            return Response({'detail': 'Город не найден'}, status=404)
        ChosenCity.objects.filter(user=self.request.user.id).filter(city_id=city_id).delete()
        return Response(status=204)
