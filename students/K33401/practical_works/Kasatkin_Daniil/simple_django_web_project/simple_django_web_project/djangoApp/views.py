from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import *


class OwnerListView(ListView):
    model = CarOwner
    template_name = 'owner_list.html'
    queryset = model.objects.all()


class OwnerCreateView(CreateView):
    model = CarOwner
    template_name = 'owner_form.html'
    fields = ['first_name', 'last_name', 'birth_date']
    success_url = '/owner_list/list/'


class CarListView(ListView):
    model = Car
    template_name = 'cars.html'
    queryset = model.objects.all()


class CarCreateView(CreateView):
    model = Car
    template_name = 'car_form.html'
    fields = ['number', 'mark', 'model', 'color']
    success_url = '/cars/'


class CarUpdateView(UpdateView):
    model = Car
    template_name = 'car_form.html'
    fields = ['number', 'mark', 'model', 'color']
    success_url = '/cars/'


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete_confirm.html'
    success_url = '/cars/'


class CarRetrieveView(DetailView):
    model = Car
    template_name = 'car_detail.html'


def list_view(request):
    context = {}
    context["dataset"] = CarOwner.objects.all()
    return render(request, "owner_list.html", context)


def create_view(request):
    context = {}
    form = CarOwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "owner_create_view.html", context)
