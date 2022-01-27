from .models import Users, Tours, Bookings
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

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