from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView

from .forms import OwnerForm
from .models import Owner, Car


def get_owner_by_id(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise get_object_or_404("Owner does not exist")
    return render(request, 'blog/owner.html', {'owner': owner})


def get_owners(request):
    data = {'owners': Owner.objects.all()}
    return render(request, 'blog/owners.html', data)


def create_owner(request):
    data = {}

    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()

    data['form'] = form
    return render(request, 'blog/owner_create.html', data)


class CarRetrieveView(DetailView):
    model = Car


class CarListView(ListView):
    model = Car


class CarUpdateView(UpdateView):
    model = Car
    template_name = 'blog/car_update.html'
    fields = ['plate', 'color']
    success_url = '/car/list'


class CarCreateView(CreateView):
    model = Car
    template_name = 'blog/car_create.html'
    fields = ['brand', 'model', 'color', 'plate']
    success_url = '/car/list'


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'blog/car_delete.html'
    success_url = '/car/list'
