from .serializer import *
from rest_framework.generics import *


class CandiesListAPIView(ListAPIView):
    serializer_class = CandiesSerializer
    queryset = Candies.objects.all()


class CandiesCreateAPIView(CreateAPIView):
    serializer_class = CandiesSerializer
    queryset = Candies.objects.all()


class CandiesRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CandiesSerializer
    queryset = Candies.objects.all()


class CandiesRetrieveAPIView(RetrieveAPIView):
    serializer_class = CandiesSerializer
    queryset = Candies.objects.all()


class ClientListAPIView(ListAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class ClientCreateAPIView(CreateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class ClientRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class ClientRetrieveAPIView(RetrieveAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class StaffListAPIView(ListAPIView):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()


class StaffCreateAPIView(CreateAPIView):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()


class StaffRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()


class StaffRetrieveAPIView(RetrieveAPIView):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()


class RequestListAPIView(ListAPIView):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()


class RequestCreateAPIView(CreateAPIView):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()