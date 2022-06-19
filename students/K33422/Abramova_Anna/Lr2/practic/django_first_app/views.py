from django.shortcuts import render, redirect
from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django_first_app.models import CarOwner, Car
from . import forms

def carowner(request, carowner_id):
    try:
        p = CarOwner.objects.get(pk=carowner_id) 
    except CarOwner.DoesNotExist:
        raise Http404("CarOwner does not exist")     
    return render(request, 'owner.html', {'CarOwner': p}) 


def all_owners(request):
    try:
        owners = CarOwner.objects.all()
    except CarOwner.DoesNotExist:
        raise Http404("CarOwners does not exist")

    return render(request, "all_owners.html", {'owners': owners})


class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


def create_owner(request):
    context = {}
    form = forms.CreateOwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/owners/")

    context['form'] = form
    return render(request, "owner_create.html", context)

def update_owner(request, pk):
    context = {}
    owner = CarOwner.objects.get(pk=pk)
    form = forms.UpdateOwnerForm(request.POST or None, instance=owner)
    if form.is_valid():
        form.save()
        return redirect("/owners/")

    context['form'] = form
    return render(request, "owner_update.html", context)

def delete_owner(request, pk):
    context = {}
    owner = CarOwner.objects.get(pk=pk)
    form = forms.OwnerDelete(request.POST or None)
    if form.is_valid():
        owner.delete() 
        return redirect("/owners/")

    context['form'] = form
    return render(request, "owner_delete.html", context)

class CarCreateView(CreateView):
    template_name = "car_create.html"
    model = Car
    fields = '__all__'
    success_url = '/cars/'


class CarUpdateView(UpdateView):
    template_name = "car_update.html"
    model = Car
    fields = '__all__'
    success_url = '/cars/'


class CarDeleteView(DeleteView):
    template_name = "car_delete.html"
    model = Car
    success_url = '/cars/'


