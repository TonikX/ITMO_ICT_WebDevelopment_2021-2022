from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render
from project_first_app.models import Owner, Car
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from .forms import OwnerForm

# Create your views here.
def owner(request, pk):
    context = {}
    context["dataset"] = Owner.objects.get(pk=pk)
    return render(request, "owner.html", context)

def owners(request):
    context = {}
    context["dataset"] = Owner.objects.all()

    form = OwnerForm(
        request.POST or None)  # создание экземпляра формы, передача в него данных из формы (из полей в браузере)
    if form.is_valid():  # проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "owners.html", context)

class CarList(ListView):
  model = Car
  template_name = 'car_list.html'

class CarViev(DetailView):
  model = Car

class CarUpdateView(UpdateView):
  model = Car
  fields = ['gos_number', 'mark', 'model', 'color']
  success_url = '/car/list/'

class CarCreateView(CreateView):
    model = Car
    fields = ['gos_number', 'mark', 'model', 'color']
    success_url = '/car/list/'

class CarDeleteView(DeleteView):
    model = Car
    success_url = '/car/list/'