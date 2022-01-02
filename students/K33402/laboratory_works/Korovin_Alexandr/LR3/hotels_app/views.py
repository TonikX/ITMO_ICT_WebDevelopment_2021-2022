from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny, IsAuthenticated


class HotelListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()

    def get_queryset(self):
        queryset = Hotel.objects.all()
        params = self.request.query_params
        end = params.get('page', None)
        title = params.get('title', None)
        sort = params.get('sort', None)
        if title:
            queryset = queryset.filter(title=title)
        if sort:
            queryset = queryset.order_by('-' + sort)
        if end:
            end = int(end)
            if end == 0:
                end = 10
                start = 0
            else:
                end = (end + 1) * 10
                start = end - 10
                queryset = queryset[start:end]
        return queryset


class CreateHotel(APIView):

    def post(self, request):
        serializer = HotelSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailHotelView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class RegisterUser(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CreateUserSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()


class ReserveHotelListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ReserveSerializer
    queryset = Reserve.objects.all()

    def get_queryset(self):
        queryset = Reserve.objects.all()
        params = self.request.query_params
        user = params.get('user', None)
        if user:
            queryset = queryset.filter(guest_id=user)
        return queryset


class CreateReserveHotelView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Reserve.objects.all()
    serializer_class = CreateReserveSerializer


class DetailReserveView(generics.RetrieveDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Reserve.objects.all()
    serializer_class = ReserveSerializer


class ReviewHotelListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def get_queryset(self):
        queryset = Review.objects.all()
        params = self.request.query_params
        hotel = params.get('hotel', None)
        if hotel:
            queryset = queryset.filter(hotel=hotel)
        return queryset


class CreateReviewHotelView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Review.objects.all()
    serializer_class = CreateReviewSerializer


class DetailReviewView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
