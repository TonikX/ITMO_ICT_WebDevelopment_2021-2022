from rest_framework import serializers
from .models import *

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class BookAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookAttachment
        fields = "__all__"

class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Readers
        fields = "__all__"


class HallsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Halls
        fields = "__all__"



class ReaderAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReaderAttachment
        fields = "__all__"

class ReaderBookAttachmentSerializer(serializers.ModelSerializer):
    attached_books = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    class Meta:
        model = Readers
        fields = "__all__"
    
