from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Car
  
class CarList(ListView):
  
    model = Car
    template_name = 'list_views_class.html'

class CarRetrieveView(DetailView):

    model = Car
    template_name = 'car_detail.html'

