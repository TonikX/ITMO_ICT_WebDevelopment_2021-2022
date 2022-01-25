from django.views.generic.list import ListView
from .models import Car
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView

class CarRetrieveView(DetailView):
  model = Car 
  template_name = 'car_detail.html'

  
class CarList(ListView):
  
    # specify the model for list view
    model = Car
    template_name = 'cvb_list_view.html'


class CarUpdateView(UpdateView):
  model = Car
  fields = ['gov_number', 'mark', 'model','colour']
  success_url = '/car_list/'
  template_name = 'carupdate.html'

class CarCreateView(CreateView):
  model = Car
  fields = ['gov_number', 'mark', 'model','colour']
  success_url = '/car_list/'
  template_name = 'carcreate.html'

class CarDeleteView(DeleteView):
  model = Car
  success_url = '/car_list/'
  template_name = 'cardelete.html'
