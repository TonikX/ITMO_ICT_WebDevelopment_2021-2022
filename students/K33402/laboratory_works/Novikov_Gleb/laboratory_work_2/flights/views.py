from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Flight, Booking


# View for Table
class FlightListView(ListView):
    template_name = "flights/flight_list.html"
    model = Flight


# View for Flight details
class FlightDetailView(DetailView):
    template_name = "flights/flight_detail.html"
    model = Flight


# View for Booking
class BookingListView(LoginRequiredMixin, ListView):
    template_name = "booking/booking_list.html"
    model = Booking
    login_url = "/signin"

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


# View for add Booking
class BookingCreateView(LoginRequiredMixin, CreateView):
    template_name = "booking/booking_add.html"
    model = Booking
    fields = ["flight", "seats"]
    success_url = "/booking_list"
    login_url = "/signin"

    def get_initial(self):
        initial = super().get_initial()
        if "flight" in self.request.GET:
            initial["flight"] = self.request.GET.get("flight")
        return initial

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# View for update Booking
class BookingUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "booking/booking_update.html"
    model = Booking
    fields = ["review_text", "review_number"]
    success_url = "/booking_list"
    login_url = "/signin"

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

