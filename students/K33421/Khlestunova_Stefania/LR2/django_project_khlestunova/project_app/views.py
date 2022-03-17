# Create your views here.
from django.shortcuts import render
from django.http import Http404
from django.views.generic.base import View
from .models import *
from .forms import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView

def user_list(request):
    data = {"users": Users.objects.all()}
    return render(request, 'users_list.html',data)

def user_create(request):
    data = {}
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
    data["form"] = form
    return render(request, 'user_create.html', data)

class ReservePlace(CreateView):
    model = Reservation
    template_name = 'reserve.html'
    success_url = '/reserve/list/'
    fields = '__all__'

class Places_List(ListView):
    template_name = 'places_list.html'
    queryset = Places.objects.all()
    paginate_by = 5

def comment(request):
    data = {}
    form = CommentForm(request.POST or None)
    if form.is_valid():
        form.save()
    data["form"] = form
    return render(request, 'comment.html', data)

def reserv_list(request):
    data = {"reservations": Reservation.objects.all}
    return render(request, 'reserv_list.html', data)

def mainpage(request):
    return render(request, 'main_page.html')

def places_list(request):
    data = {"planes": Plane.objects.all, "reservations": Reservation.objects.all, "places": Places.objects.all}
    return render(request, 'passenger_list_view.html', data)

class ReservationUpdate(UpdateView):
    model = Reservation
    template_name = 'reserv_up.html'
    success_url = '/reserve/list/'
    fields = '__all__'

    def get_object(self):
        return get_object_or_404(Reservation, id=self.kwargs.get('pk'))

class ReservationDelete(DeleteView):
    model = Reservation
    template_name = 'reserv_del.html'
    success_url = '/reserve/list/'

class PassengerList(ListView):
    queryset = Reservation.objects.all()
    template_name = 'passenger_list_view.html'

class ESearchView(View):
    template_name = 'search_form.html'

    def get(self, request, *args, **kwargs):
        context = {}

        question = request.GET.get('q')
        if question is not None:
            search_places = Places.objects.filter(p_number=question)

            # формируем строку URL, которая будет содержать последний запрос
            # Это важно для корректной работы пагинации
            context['last_question'] = '?q=%s' % question

            current_page = Paginator(search_places, 10)

            page = request.GET.get('page')
            try:
                context['places'] = current_page.page(page)
            except PageNotAnInteger:
                context['places'] = current_page.page(1)
            except EmptyPage:
                context['places'] = current_page.page(current_page.num_pages)

        return render(request, template_name=self.template_name, context=context)