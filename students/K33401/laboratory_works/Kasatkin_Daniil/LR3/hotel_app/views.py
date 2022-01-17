from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import filters


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['phone_number'] = user.phone_number
        token['is_host'] = user.is_host
        token['first_name'] = user.first_name
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@permission_classes([AllowAny])
class CreateUser(APIView):
    def post(self, request):
        seralizer = CreateUserSerializer(data=request.data)
        if seralizer.is_valid():
            user = seralizer.save()
            if user:
                return Response(status=status.HTTP_201_CREATED)
        return Response(seralizer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
class CreateHostUser(generics.UpdateAPIView):
    serializer_class = CreateHostUserSerializer
    queryset = User.objects.all()


@permission_classes([AllowAny])
class PlaceListView(generics.ListAPIView):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()


@permission_classes([AllowAny])
class PlaceListFilter(generics.ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^title']


@permission_classes([AllowAny])
class PlaceRetrieveView(generics.RetrieveAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


@permission_classes([IsAuthenticated])
class CreatePlaceView(APIView):
    def post(self, request):
        seralizer = CreatePlaceSerializer(data=request.data)
        print(seralizer)
        if seralizer.is_valid():
            place = seralizer.save()
            if place:
                return Response(status=status.HTTP_201_CREATED)
        return Response(seralizer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReserveListView(generics.ListAPIView):
    serializer_class = ReserveSerializer

    def get_queryset(self):
        queryset = Reserve.objects.all()
        params = self.request.query_params
        guest = params.get('guest', None)
        place_id = params.get('place_id', None)
        dates = params.get('dates', None)

        if guest:
            queryset = queryset.filter(guest=guest)
        if place_id:
            queryset = queryset.filter(place_id=place_id)
        if dates and place_id:
            dates = dates.split(',')
            check_in_date = dates[0]
            check_out_date = dates[1]
            filter_params = dict(check_in_date__lte=check_out_date, check_out_date__gte=check_in_date)
            queryset = Reserve.objects.filter(**filter_params, place_id=place_id)
        return queryset


@permission_classes([IsAuthenticated])
class ReserveRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserve.objects.all()
    serializer_class = CreateReserveSerializer

@permission_classes([IsAuthenticated])
class CreateReserveView(generics.CreateAPIView):
    queryset = Reserve.objects.all()
    serializer_class = CreateReserveSerializer


@permission_classes([AllowAny])
class ReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        queryset = Review.objects.all()
        params = self.request.query_params
        place = params.get('place', None)
        author = params.get('author', None)
        if author:
            queryset = queryset.filter(author_id=author)
        if place:
            queryset = queryset.filter(place_id=place)
        return queryset


@permission_classes([IsAuthenticated])
class ReviewRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = CreateReviewSerializer


@permission_classes([IsAuthenticated])
class CreateReviewView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = CreateReviewSerializer
