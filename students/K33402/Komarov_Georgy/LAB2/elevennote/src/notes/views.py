from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.urls import reverse, reverse_lazy

from .models import Note
from .forms import NoteForm
from .mixins import NoteMixin
from django.db.models import Q


class NoteList(LoginRequiredMixin, ListView):
    paginate_by = 5
    template_name = 'notes/index.html'
    context_object_name = 'latest_note_list'

    def get_queryset(self):
        users_filter = Q(owner=self.request.user) | Q(shared=self.request.user)

        if title := self.request.GET.get('title'):
            return Note.objects.filter(users_filter, title__icontains=title).order_by('-pub_date').distinct()
        if tag := self.request.GET.get('tag'):
            return Note.objects.filter(users_filter, tags__name=tag).order_by('-pub_date').distinct()
        return Note.objects.filter(users_filter).order_by('-pub_date').distinct()


class NoteDetail(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'notes/detail.html'
    context_object_name = 'note'

    def get_queryset(self):
        return Note.objects.filter(Q(owner=self.request.user) | Q(shared=self.request.user)).order_by(
            '-pub_date').distinct()


class NoteCreate(LoginRequiredMixin, NoteMixin, CreateView):
    form_class = NoteForm
    template_name = 'notes/form.html'
    success_url = reverse_lazy('notes:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(NoteCreate, self).form_valid(form)


class NoteUpdate(LoginRequiredMixin, NoteMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/form.html'

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)

    def get_success_url(self):
        return reverse('notes:update', kwargs={
            'pk': self.object.pk
        })


class NoteDelete(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('notes:create')

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)
