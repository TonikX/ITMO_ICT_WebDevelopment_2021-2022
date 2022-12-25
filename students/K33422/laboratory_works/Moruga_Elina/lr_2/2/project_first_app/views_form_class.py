from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from .models import Car

class CarsUpdateView(UpdateView):
  model = Car
  fields = ['gov_no', 'brand', 'model', 'color', 'owners']
  success_url = '/cars/list/'
  template_name = 'car_form.html'

class CarCreateView(CreateView):
  model = Car
  fields = ['gov_no', 'brand', 'model', 'color', 'owners']
  success_url = '/cars/list/'
  template_name = 'car_form.html'

class CarDeleteView(DeleteView):
  model = Car
  success_url = '/cars/list/'
  template_name = 'car_confirm_delete.html'

