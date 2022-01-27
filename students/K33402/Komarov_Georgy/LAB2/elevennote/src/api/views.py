from django.db.models import Q
from rest_framework import viewsets

from notes.models import Note
from .serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

    def filter_queryset(self, queryset):
        users_filter = Q(owner=self.request.user) | Q(shared=self.request.user)

        if getattr(self.request, 'GET'):  # listing
            if title := self.request.GET.get('title'):
                return Note.objects.filter(users_filter, title__icontains=title).order_by('-pub_date').distinct()
            if tag := self.request.GET.get('tag'):
                return Note.objects.filter(users_filter, tags__name=tag).order_by('-pub_date').distinct()
            return Note.objects.filter(users_filter).order_by('-pub_date').distinct()
        else:  # editing
            return Note.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
