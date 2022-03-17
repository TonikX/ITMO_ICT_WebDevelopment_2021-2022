from datetime import timedelta

from django.db.models import Q
from django.views.generic.edit import UpdateView, DeleteView

from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404

from .models import *
from .forms import *

def hotel(request, h_id):
    try:
        hot = Hotel.objects.get(pk=h_id)
    except Hotel.DoesNotExist:
        raise Http404("Hotel does not exist")
    return render(request, 'hotel.html', {'hotel': hot})


def hotel_list(request):
    context = {"hotels": Hotel.objects.all(), "all": True}
    return render(request, 'hotel_list.html', context)

def room_list(request, h_id):
    hotel = Hotel.objects.get(pk=h_id)
    rooms = Room.objects.filter(hotel=hotel)
    return render(request, 'room_list.html', {'hotel': hotel, 'rooms': rooms})

def room(request, h_id, r_id):
    hotel = Hotel.objects.get(pk=h_id)
    room = Room.objects.get(pk=r_id)
    return render(request, "room.html", {'hotel': hotel, 'room': room})


def reservation(request, h_id, r_id):
    room = get_object_or_404(Room, id=r_id)
    hotel = get_object_or_404(Hotel, id=h_id)
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            res = form.save(commit=False)
            res.user = request.user
            res.room = room
            res.save()
            return redirect('/profile/')
    else:
        form = ReservationForm()
    return render(request, 'reservation.html', {'form': form, 'room': room,'hotel': hotel})

def user_list(request, h_id):
    hotel = get_object_or_404(Hotel, id=h_id)
    now = datetime.now()
    month = datetime.now() - timedelta(days=30)
    reserves = Reservation.objects.filter(room__hotel=hotel)\
        .filter(Q(departure__range=[month,now]) | Q(arrival__range=[month,now]))
    return render(request, 'user_list.html', {'reserves': reserves, 'hotel': hotel})

def mainpage(request):
    return render(request, 'mainpage.html')

class DeleteReservation(DeleteView):
  model = Reservation
  success_url = '/profile/'
  template_name = 'del_res.html'

class UpdateReservation(UpdateView):
    model = Reservation
    fields = ['arrival', 'departure']
    success_url = '/profile/'
    template_name = 'upd_res.html'



