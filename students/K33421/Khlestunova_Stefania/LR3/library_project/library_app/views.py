from django.db.models import *
from .serializers import *
from rest_framework import generics
from .models import *
from datetime import date, timedelta
# Create your views here.

class BookListAPIView(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class BookCreateAPIView(generics.CreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class ReaderListAPIView(generics.ListAPIView):
    serializer_class = ReaderSerializer

    def get_queryset(self):
        queryset = Readers.objects.all()
        params = self.request.query_params

        age_lte = params.get('age_l', None)
        age_gte = params.get('age_g', None)
        instances_lte = params.get('instances_lte', None)
        instances_gte = params.get('instances_gte', None)
        to_date = params.get('to_date', None)
        from_date = params.get('from_date', None)
        
        if to_date:
            bookset = Book.objects.filter(bookattachment__in=BookAttachment.objects.filter(attach_date__lte=to_date))
            queryset = Readers.objects.filter(attached_books__in=bookset).distinct()
        if from_date:
            bookset = Book.objects.filter(bookattachment__in=BookAttachment.objects.filter(attach_date__gte=from_date))
            queryset = Readers.objects.filter(attached_books__in=bookset).distinct()
        if age_lte:
            queryset = Readers.objects.filter(birth_date__lte=date.today()-timedelta(days=365*int(age_lte)))
            print(f"Количество читателей старше {age_lte} = {queryset.count()}")
        if age_gte:
            queryset = Readers.objects.filter(birth_date__gte=date.today()-timedelta(days=365*int(age_gte)))
            print(f"Количество читателей младше {age_gte} = {queryset.count()}")
        if instances_lte:
            queryset = Readers.objects.filter(attached_books__instance_count__lte=instances_lte)
        if instances_gte:
            queryset = Readers.objects.filter(attached_books__instance_count__gte=instances_gte)
        return queryset

class HallsListAPIView(generics.ListAPIView):
    serializer_class = HallsSerializer
    queryset = Halls.objects.all()

class HallsCreateAPIView(generics.CreateAPIView):
    serializer_class = HallsSerializer
    queryset = Halls.objects.all()


class HallsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HallsSerializer
    queryset = Halls.objects.all()


class ReadersAttachmentAPIView(generics.ListAPIView):
    serializer_class = ReaderAttachmentSerializer
    queryset = ReaderAttachment.objects.all()

class ReadersAttachmentCreateAPIView(generics.CreateAPIView):
    serializer_class = ReaderAttachmentSerializer
    queryset = ReaderAttachment.objects.all()

class ReadersAttachmentRetrieveUpdateDestriyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReaderAttachmentSerializer
    queryset = ReaderAttachment.objects.all()

class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class ReaderRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ReaderSerializer
    queryset = Readers.objects.all()

class ReaderCreateAPIView(generics.CreateAPIView):
    serializer_class = ReaderSerializer
    queryset = Readers.objects.all()


class ReaderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReaderSerializer
    queryset = Readers.objects.all()

class BookAttachmentListAPIView(generics.ListAPIView):
    serializer_class = BookAttachmentSerializer

    
    def get_queryset(self):
        queryset = BookAttachment.objects.all()
        params = self.request.query_params

        to_date = params.get('to_date', None)
        from_date = params.get('from_date', None)
        if to_date:
            queryset = BookAttachment.objects.filter(attach_date__lte=to_date)
        if from_date:
            queryset = BookAttachment.objects.filter(attach_date__gte=from_date)
        
        return queryset

class BookAttachmentCreateAPIView(generics.CreateAPIView):
    serializer_class = BookAttachmentSerializer
    queryset = BookAttachment.objects.all()


class BookAttachmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookAttachmentSerializer
    queryset = BookAttachment.objects.all()


class ReaderBookRelated(generics.RetrieveAPIView):
    serializer_class = ReaderBookAttachmentSerializer
    queryset = Readers.objects.all()

