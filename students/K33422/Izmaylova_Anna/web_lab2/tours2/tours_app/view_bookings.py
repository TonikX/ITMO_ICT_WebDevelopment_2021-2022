from .models import Users, Tours, Bookings
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Bookings
from django.views.generic.edit import UpdateView, CreateView, DeleteView

# представление для списка бронирований
class Booked(LoginRequiredMixin, ListView):
    model = Bookings
    template_name = 'bookings.html'
    queryset = model.objects.all()
 
    def get_queryset(self):
        tour = self.request.GET.get('tour')
    
        if tour:
            user = Users.objects.all().filter(username=self.request.user)
            tour = Tours.objects.all().filter(id=tour)
    
            Bookings.objects.create(id_user=user[0], id_tour=tour[0])
    
        return self.queryset.filter(id_user=self.request.user)

# создать бронирование
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
