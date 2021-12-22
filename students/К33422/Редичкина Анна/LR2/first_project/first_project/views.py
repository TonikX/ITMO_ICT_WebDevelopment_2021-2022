from django.http import Http404
from django.shortcuts import render
from first_project.models import Owner, Car
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from .forms import OwnerForm


def owner(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404('Owner does not exist')

    return render(request, 'owner.html', {'owner': owner})


def owner_list(request):
    data = {"owners": Owner.objects.all()}
    return render(request, "owners.html", data)


def owner_create(request):
    data = {}
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    data["form"] = form
    return render(request, "owner_create.html", data)


class CarRetrieveView(DetailView):
    model = Car
    template_name = 'car_detail.html'


class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'


class CarCreateView(CreateView):
    model = Car
    template_name = "car_create.html"
    fields = ["number", "brand", "model", "color"]
    success_url = "/car/list"


class CarUpdateView(UpdateView):
    model = Car
    template_name = "car_update.html"
    fields = ["number", "brand", "model", "color"]
    success_url = "/car/list"


class CarDeleteView(DeleteView):
    model = Car
    template_name = "car_delete.html"
    success_url = "/car/list"
