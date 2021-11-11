from django.views.generic.edit import CreateView
from .models import Car

class CarUpdateView(CreateView):
  model = Car
  fields = ['gov_no', 'brand', 'model', 'color', 'owners']
  success_url = '/cars/list/'
  template_name = 'car_form.html'