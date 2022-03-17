from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from project_first_app.models import Owner, Car
from project_first_app.forms import Create_owner_form


def owner_id(request, id_owner):

    try:
        p = Owner.objects.get(pk=id_owner)
    except Owner.DoesNotExist:
        raise Http404('Owner does not exist')

    return render(request, 'owner.html', {'owner': p})


def owners_all(request):

    context = {}
    context['dataset'] = Owner.objects.all()

    return render(request, 'all_owners.html', context)


class Cars_all(ListView):

    model = Car
    template_name = 'all_cars.html'


class Car_id(DetailView):

    model = Car
    template_name = 'project_first_app/car.html'


def owner_create(request):

    context = {}
    form = Create_owner_form(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form

    return render(request, 'project_first_app/create_owner.html', context)


class Car_create(CreateView):

    model = Car
    template_name = 'project_first_app/create_car.html'
    fields = ['number_car', 'brand_car', 'model_car', 'color_car']
    success_url = '/all_cars'


class Car_update(UpdateView):

    model = Car
    template_name = 'project_first_app/update_car.html'
    fields = ['number_car', 'color_car']
    success_url = '/all_cars'


class Car_delete(DeleteView):

    model = Car
    template_name = 'project_first_app/delete_car.html'
    success_url = '/all_cars'
