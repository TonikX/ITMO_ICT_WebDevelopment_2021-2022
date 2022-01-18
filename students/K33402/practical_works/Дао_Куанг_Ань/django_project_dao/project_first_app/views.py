from django.http import Http404, HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from project_first_app.forms import OwnerForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from project_first_app.models import Owner, Car
import datetime


# Create your views here.
def detail1(request):
    p = {}
    try:
        p['owner'] = Owner.objects.all()
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', p)


def detail2(request, id):
    p2 = {}
    try:
        p2['owner'] = Owner.objects.get(id=id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner2.html', p2)


def time_view(request):
    now = datetime.datetime.now()
    html = "Time is {}".format(now)
    return HttpResponse(html)


class CarView(ListView):
    # specify the model for list view
    model = Car
    template_name = 'car.html'


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


class CarListView(ListView):
    model = Car
    template_name = 'carlistview.html'
    queryset = model.objects.all()

    def get_queryset(self):
        id = self.request.GET.get('id')

        if id:
            try:
                id = int(id)
                queryset = self.queryset.filter(id=id)

            except ValueError:
                queryset = self.model.objects.none()

            return queryset

        return self.queryset


def owner_post(request):
    context = {}
    form = OwnerForm(request.POST or None)
    if form.is_valid():  # проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "owner_post.html", context)


class CarUpdateView(UpdateView):
    model = Car
    template_name = 'car_update.html'
    fields = ['state_number', 'brand', 'model', 'color']
    success_url = '/car/list/'


class CarCreateView(CreateView):
    model = Car
    template_name = 'car_create.html'
    fields = ['state_number', 'brand', 'model', 'color']


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/car/list/'