from rest_framework import status
from rest_framework.response import Response

from .serializers import *
from rest_framework.generics import *


class BookListAPIView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookCreateAPIView(CreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookRetrieveAPIView(RetrieveAPIView):
    serializer_class = BookRetrieveSerializer
    queryset = Book.objects.all()


class ReaderListAPIView(ListAPIView):
    serializer_class = ReaderSerializer
    queryset = Reader.objects.all()


class ReaderCreateAPIView(CreateAPIView):
    serializer_class = ReaderSerializer
    queryset = Reader.objects.all()


class ReaderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ReaderSerializer
    queryset = Reader.objects.all()


class ReaderRetrieveAPIView(RetrieveAPIView):
    serializer_class = ReaderRetrieveSerializer
    queryset = Reader.objects.all()


# class ReportApiView(ListAPIView):
#     serializer_class = ReportSerializer
#
#     books_by_hall = list(BookInHall.objects.annotate(books_by_hall=Sum('count')))
#     print(books_by_hall)
#     # books_total = sum([v['books_by_hall'] for v in books_by_hall])

# queryset = QuerySet([{'books_by_hall': books_by_hall}, {'books_total': books_total}])
# print(queryset)


class ReaderBookCreateAPIView(CreateAPIView):
    serializer_class = ReaderBookCreateSerializer
    queryset = ReaderBook.objects.all()


class ReaderBookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ReaderBookSerializer
    queryset = ReaderBook.objects.all()

    # def destroy_list(self, request, *args, **kwargs):
    #     self.get_queryset().delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class ReaderBookListAPIView(ListAPIView):
    serializer_class = ReaderBookSerializer
    queryset = ReaderBook.objects.all()


class ReaderBookRetrieveAPIView(RetrieveAPIView):
    serializer_class = ReaderBookSerializer
    queryset = ReaderBook.objects.all()
