from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.paginator import Paginator

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .models import *
from .forms import *


#homepage
class Homepage(TemplateView):
    template_name = 'index.html'


# create user
def register(request):
    if request.user.is_authenticated:
        return redirect('/reservation/')
    else:
        form = UserForm()
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()

                return redirect('login')

        data = {'form': form}
        return render(request, 'register.html', data)


#login
def login_(request):
    if request.user.is_authenticated:
        return redirect('/reservation/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/reservation/')

        data = {}
        return render(request, 'login.html', data)


#logout
def logout_(request):
    logout(request)
    return redirect('login')


#reservation list
class ListReservation(ListView):
    model = Reservation
    template_name = 'reservation.html'
    all_reservations = Reservation.objects
    paginate_by = 2

    def get_queryset(self):
        return Reservation.objects.all()


# create reservation
class ReservationCreateView(CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservation_create.html'


# view reservation
class ReservationRetrieveView(DetailView):
    model = Reservation
    template_name = 'reservation_detail.html'


# update reservation data
class ReservationUpdateView(UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservation_update.html'


# delete reservation
class ReservationDeleteView(DeleteView):
    model = Reservation
    template_name = 'reservation_delete.html'


# hotels list
class HotelList(ListView):
    model = Hotel
    template_name = 'hotel.html'
    all_hotels = Hotel.objects
    paginate_by = 3


# hotel view
class HotelRetriveView(DetailView):
    model = Hotel
    template_name = 'hotel_detail.html'


# write review
class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review.html'


#review list
class ReviewList(ListView):
    model = Review
    template_name = 'review_list.html'
    all_reviews = Review.objects
    paginate_by = 3


#guests list
class GuestsList(ListView):
    model = Reservation
    template_name = 'guests.html'