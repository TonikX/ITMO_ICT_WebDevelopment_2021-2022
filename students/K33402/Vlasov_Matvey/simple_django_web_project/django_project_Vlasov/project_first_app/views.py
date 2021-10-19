from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from .forms import OwnerForm
from .models import OwnerUser, Car


def show_owner(request, owner_id):
    try:
        owner = OwnerUser.objects.get(pk=owner_id)
    except OwnerUser.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'project_first_app/owner.html', {'owner': owner})


def list_owners(request):
    data = {'owners': OwnerUser.objects.all()}
    return render(request, 'project_first_app/owner_list.html', data)


def create_owner(request):
    data = {}

    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()

    data['form'] = form
    return render(request, 'project_first_app/create_owner.html', data)


class CarRetrieveView(DetailView):
    model = Car


class CarListView(ListView):
    model = Car


class CarUpdateView(UpdateView):
    model = Car
    template_name = 'project_first_app/car_update.html'
    fields = ['plate', 'color']
    success_url = '/car/list'


class CarCreateView(CreateView):
    model = Car
    template_name = 'project_first_app/car_create.html'
    fields = ['plate', 'make', 'model', 'color']
    success_url = '/car/list'


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'project_first_app/car_delete.html'
    success_url = '/car/list'
