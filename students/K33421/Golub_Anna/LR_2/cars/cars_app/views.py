from django.http import Http404
from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import User, Car
from .forms import OwnerForm


# get owner by id
def owner(request, owner_id):
    try:
        ow = User.objects.get(pk=owner_id)
    except User.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner_detail.html', {'owner': ow})


# list all owners
def owner_list(request):
    context = dict()
    context["dataset"] = User.objects.all()
    return render(request, "owner_list_view.html", context)


# create owner
def owner_create(request):
    context = dict()
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = OwnerForm()
    context['form'] = form
    return render(request, "owner_create.html", context)


# get car by id
class CarRetrieveView(DetailView):
    model = Car


# list all cars
class CarList(ListView):
    model = Car
    template_name = 'car_list_view.html'


# create car
class CarCreateView(CreateView):
    model = Car
    fields = ['number', 'brand', 'model', 'color']
    success_url = '/car/list/'


# delete car
class CarDeleteView(DeleteView):
    model = Car
    success_url = '/car/list/'


# update car data
class CarUpdateView(UpdateView):
    model = Car
    fields = ['number', 'brand', 'model', 'color']
    success_url = '/car/list/'
