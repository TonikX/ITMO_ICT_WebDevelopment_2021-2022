from django.shortcuts import render

# Create your views here.

from django.http import Http404
from cars.models import Car_owner, Car
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from cars.forms import CarOwnerCreateForm

def car_owner_info(request, car_owner_id):
    try:
        o = Car_owner.objects.get(pk=car_owner_id)
    except Car_owner.DoesNotExist:
        raise Http404("Car owner does not exist")
    return render(request, 'cars/owner.html', {'car_owner': o})

def all_owners(request):
    context = {}
    context["owners"] = Car_owner.objects.all()
    return render(request, 'cars/all_owners.html', context)

def car_owner_create(request):
    context = {}
    form = CarOwnerCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
    context["form"] = form
    return render(request, "cars/owner_create.html", context)


class AllCars(ListView):
    model = Car
    template_name = 'cars/all_cars.html'


class CarInfo(DetailView):
    model = Car
    template_name = 'cars/car.html'

class CarUpdate(UpdateView):
    model = Car
    template_name = 'cars/car_update.html'
    fields = ['car_number', 'colour']
    success_url = '/all_cars/'

class CarCreate(CreateView):
    model = Car
    template_name = 'cars/car_create.html'
    fields = ['car_number', 'brand', 'model', 'colour']
    success_url = '/all_cars/'

class CarDelete(DeleteView):
    model = Car
    template_name = 'cars/car_delete.html'
    success_url = '/all_cars/'
