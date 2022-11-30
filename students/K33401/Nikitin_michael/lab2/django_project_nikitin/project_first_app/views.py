from django.shortcuts import render, redirect
from django.http import Http404
from django.shortcuts import render
from .models import Car, Driver
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .forms import DriverForm

def start_page(request):
    return render(request, 'start_page.html')


def get_owner_by_id(request, owner_id):
    try:
        owner = Driver.objects.get(pk=owner_id)
    except Driver.DoesNotExist:
        raise Http404("such owner doesn't exist")
    return render(request, 'owner_id.html', {"owner": owner})


def get_new_owner(request):
    context = {}

    form = DriverForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/owners/all')
    context['form'] = form
    return render(request, 'create_owner.html', context)


def get_all_owners(request):
    all = {}
    all["owners"] = Driver.objects.all()
    return render(request, 'all_owners.html', all)


class CarsList(ListView):
    model = Car
    template_name = 'car.html'


class CarsCreate(CreateView):
    model = Car
    fields = ['plate', 'brand', 'model', 'color']
    template_name = 'car_create.html'
    success_url = '/cars/'


class CarsRead(DetailView):
    model = Car
    template_name = 'car_read.html'



class CarsUpdate(UpdateView):
    model = Car
    fields = ['plate', 'brand', 'model', 'color']
    template_name = 'car_upd.html'
    success_url = '/cars/'


class CarsDelete(DeleteView):
    model = Car
    template_name = 'car_del.html'
    success_url = '/cars/'



