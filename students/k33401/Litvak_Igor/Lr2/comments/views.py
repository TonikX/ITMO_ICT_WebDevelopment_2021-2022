from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from comments.models import Comment
from bookings.models import Booking


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['text', 'rating']
    template_name = 'create_comment.html'
    success_url = reverse_lazy('booking-list')

    def form_valid(self, form):
        pk = self.request.GET['booking']
        form.instance.booking = get_object_or_404(Booking, pk=pk)
        return super(CommentCreateView, self).form_valid(form)
