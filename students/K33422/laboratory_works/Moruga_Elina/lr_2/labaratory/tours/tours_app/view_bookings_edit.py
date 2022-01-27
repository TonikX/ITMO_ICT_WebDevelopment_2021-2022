from .models import Bookings
from django.views.generic.edit import UpdateView, CreateView, DeleteView

class MakeReservation(CreateView):
    model = Bookings
    template_name = 'bookings_make.html'
    fields = ['id_user', 'id_tour']
    success_url = '/bookings_list/'

class DeleteReservation(DeleteView):
    model = Bookings
    template_name = 'bookings_delete.html'
    success_url = '/bookings_list/'

class EditReservation(UpdateView):
    model = Bookings
    template_name = 'bookings_edit.html'
    fields = ['id_user', 'id_tour']
    success_url = '/bookings_list/'

