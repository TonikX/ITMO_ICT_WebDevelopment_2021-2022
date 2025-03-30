from django.shortcuts import render
from django.http import Http404
from .models import CarOwner, Car
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CarOwnerForm

# Create your views here.

def owner(request, ow_id):
    try:
        ow = CarOwner.objects.get(pk=ow_id)
    except CarOwner.DoesNotExist:
        raise Http404("Car owner does not exist")
    return render(request, 'owner.html', {'owner': ow})

def owners_list(request):
    context = {"owners": CarOwner.objects.all(), "all": True}
    return render(request, 'owners.html', context)

class CarsList(ListView):
    model = Car
    template_name = "cars.html"

class CarId(DetailView):
    model = Car
    template_name = "car.html"


def create_view(request):
    context = {}
    form = CarOwnerForm(
        request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_view.html", context)


class CarUpdate(UpdateView):
    model = Car
    fields = ['gos_num', 'brand', 'model', 'color']
    success_url = '/cars_list/'
    template_name = 'car_upd.html'


class CarCreate(CreateView):
    model = Car
    fields = ['gos_num', 'brand', 'model', 'color']
    success_url = '/cars_list/'
    template_name = 'car_create.html'

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars_list/'
    template_name = 'car_delete.html'
