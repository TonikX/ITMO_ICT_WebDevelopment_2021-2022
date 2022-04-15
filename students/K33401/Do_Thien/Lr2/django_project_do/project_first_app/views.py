from django.db.models import query
from django.http import Http404
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.edit import DeleteView


from .models import Owner, Driver_license, Car
from .forms import ExampleForm
import datetime


def detail(request):
    try:
        context = {}
        context["dataset"] = Owner.objects.all()
    except:
        raise Http404("Owner doesn't exist")

    return render(request, 'owner.html', context)


def detail_view(request, id):
    context2 = {}
    context2["data"] = Owner.objects.get(id = id)

    return render(request, "detail_view.html", context2)
  

def example_view(request):
    now = datetime.datetime.now()
    html = "Time is {}".format(now)
    return HttpResponse(html)


class ExampleList(ListView):
    model = Car
    template_name = 'list_view.html'


class CarRetrieveView(DetailView):
    model = Car
    template_name = 'car_detail.html'



class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'
    queryset = model.objects.all()

    def get_queryset(self):
        car = self.request.GET.get('id')
    
        if car:

            try:
                car = int(car)
                queryset = self.queryset.filter(id=car)
            except ValueError:
                queryset = self.model.objects.none()

            return queryset

        return self.queryset


def CreateViewCar(request):
    context ={}
    form = ExampleForm(request.POST or None) 
    if form.is_valid(): 
        form.save()
    context['form'] = form
    return render(request, "create_view.html", context)


class CarUpdateView(UpdateView):
    model = Car
    template_name = 'car_form.html'
    fields = ['license_plate', 'brand', 'model', 'color']
    success_url = '/car/list/'

class CarCreateView(CreateView):
    model = Car
    template_name = 'car_create.html'
    fields = ['license_plate', 'brand', 'model', 'color']


class CarDeleteView(DeleteView):
  model = Car
  template_name = 'car_delete.html'
  success_url = '/car/list/'