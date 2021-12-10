from datetime import datetime, timedelta
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView, DeleteView
from bookings.models import Booking


class IndexView(ListView):
    model = Booking
    template_name = 'index.html'

    def get_queryset(self):
        return Booking.objects.filter(
            booking_date__gte=datetime.now() - timedelta(days=10)).order_by('-booking_date')[:10]


class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'list_bookings.html'

    def get_queryset(self):
        return Booking.objects.filter(by=self.request.user)


class BookingDetailView(LoginRequiredMixin, DetailView):
    model = Booking
    template_name = 'view_booking.html'


class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    fields = ['room', 'start', 'end']
    template_name = 'create_booking.html'
    success_url = reverse_lazy('booking-list')

    def form_valid(self, form):
        form.instance.by = self.request.user
        return super(BookingCreateView, self).form_valid(form)

    def get_initial(self):
        # Fill in value for room if it is passed in url
        initial = super(BookingCreateView, self).get_initial()
        if 'room' in self.request.GET:
            initial['room'] = self.request.GET.get('room')
        return initial


class BookingDeleteView(LoginRequiredMixin, DeleteView):
    model = Booking
    template_name = 'delete_booking.html'
    success_url = reverse_lazy('booking-list')

    def delete(self, request, *args, **kwargs):
        # Only allow the creator of booking to delete it
        if self.get_object().by == request.user:
            return super(BookingDeleteView, self).delete(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You can't cancel this booking")
