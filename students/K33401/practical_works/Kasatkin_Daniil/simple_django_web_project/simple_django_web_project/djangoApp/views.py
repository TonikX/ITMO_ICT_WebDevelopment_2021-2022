from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *


class OwnerRetrieveView(DetailView):
    model = CarOwner


class OwnerListView(ListView):
    model = CarOwner
    template_name = 'owner_list.html'
    queryset = model.objects.all()


class OwnerUpdateView(UpdateView):
    model = CarOwner
    template_name = 'owner_list.html'
    fields = ['first_name', 'last_name', 'birth_date']
    success_url = '/owner_list/list/'


class OwnerCreateView(CreateView):
    model = CarOwner
    template_name = 'owner_form.html'
    fields = ['first_name', 'last_name', 'birth_date']
    success_url = '/owner_list/list/'


class OwnerDeleteView(DeleteView):
    model = CarOwner
    template_name = 'owner_list.html'
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


class CarRetrieveView(DetailView):
    model = Car
    template_name = 'car_detail.html'

