from typing import List
from django.template.response import TemplateResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.http import Http404
from .models import Owner, Car
from .forms import Owner_Form

def owner(request, owner_id):
    try:
        o = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'owner': o})


class Car_List(ListView):
    model = Car
    template_name = 'cars_list.html'


class One_Car(DetailView):
    model = Car
    template_name = 'car_detail.html'


def create_view(request):
    context = {}
    form = Owner_Form(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_view.html", context)


class Car_Update(UpdateView):
    model = Car
    fields = ['number', 'brand', 'model', 'colour']
    success_url = '/car/'
    template_name = 'car_form.html'


class Car_Create(CreateView):
    model = Car
    template_name = 'create_car.html'
    success_url = '/car/'
    fields = ['number', 'brand', 'model', 'colour']

class Car_Delete(DeleteView):
    model = Car
    success_url = '/car/'
    template_name = 'delete_car.html'