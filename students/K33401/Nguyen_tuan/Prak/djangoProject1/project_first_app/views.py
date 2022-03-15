from django.http import Http404
from django.shortcuts import render
from project_first_app.models import Car_Owner, Car
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from project_first_app.forms import ExampleForm
from django.views.generic.edit import UpdateView, DeleteView, CreateView

def detail(request, id):
    p = {}
    try:
        p['dataset'] = Car_Owner.objects.get(pk = id)
    except Car_Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'Car_Owner.html', p)
def detail1(request):
    q = {}
    try:
        q['dataset'] = Car_Owner.objects.all()
    except Car_Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'Car_Owner1.html', q)
class ExamplelistCar(ListView):
    model = Car
    template_name = 'cvb_list_view.html'
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


def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}
    # add the dictionary during initialization
    form = ExampleForm(request.POST or None)  # создание экземпляра формы, передача в него данных из формы (из полей в браузере)
    if form.is_valid():  # проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "create_view.html", context)
class CarCreateView(CreateView):
  model = Car
  template_name = 'car_createbyclass.html'
  fields = ['state_number', 'brand', 'model', 'Color']
  success_url = '/car/list/'
class CarUpdateView(UpdateView):
  model = Car
  template_name = 'car_form.html'
  fields = ['state_number', 'brand', 'model', 'Color']
  success_url = '/car/list/'
class CarDeleteView(DeleteView):
  model = Car
  template_name = 'car_confirm_delete.html'
  success_url = '/Car/list/'