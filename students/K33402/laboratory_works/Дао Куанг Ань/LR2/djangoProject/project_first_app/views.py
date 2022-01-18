from django.http import Http404
from django.shortcuts import render
from .models import *
import datetime
from django.views.generic.edit import UpdateView, DeleteView, CreateView


def room(request):
    r = {}
    try:
        r['rooms'] = Room.objects.all()
    except Room.DoesNotExist:
        raise Http404("Room does not exist")
    return render(request, 'room.html', r)


def client_id(request, id):
    c = {}
    try:
        c['clients'] = Client.objects.get(pk=id)
    except Client.DoesNotExist:
        raise Http404("Client does not exist")
    return render(request, 'client_id.html', c)


def client(request):
    c = {}
    try:
        c['clients'] = Client.objects.all()[1:]
    except Client.DoesNotExist:
        raise Http404("Client does not exist")
    return render(request, 'client.html', c)


def bill(request):
    b = {}
    try:
        b['bills'] = Bill.objects.all()
    except Bill.DoesNotExist:
        raise Http404("Bill does not exist")
    return render(request, 'bill.html', b)


def fb(request):
    f = {}
    try:
        f['fbs'] = Feedback.objects.all()
    except Feedback.DoesNotExist:
        raise Http404("Feedback does not exist")
    return render(request, 'fb.html', f)


class BillCreateView(CreateView):
    model = Bill
    template_name = 'create_bill.html'
    fields = ['date_checkin', 'date_checkout', 'time_checkin', 'time_checkout', 'id_room', 'id_client']
    success_url = '/bill/'


class BillUpdateView(UpdateView):
    model = Bill
    template_name = 'update_bill.html'
    fields = ['date_checkin', 'date_checkout', 'time_checkin', 'time_checkout', 'id_room', 'id_client']
    success_url = '/bill/'


class BillDeleteView(DeleteView):
    model = Bill
    template_name = 'delete_bill.html'
    success_url = '/bill/'


class ClientCreateView(CreateView):
    model = Client
    template_name = 'create_client.html'
    fields = ['first_name', 'last_name', 'birthdate', 'sex', 'tel', 'passport']
    success_url = '/client/'


class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'update_client.html'
    fields = ['first_name', 'last_name', 'birthdate', 'sex', 'tel', 'passport']
    success_url = '/client/'


class FeedbackCreateView(CreateView):
    model = Feedback
    template_name = 'create_fb.html'
    fields = ['rating', 'comment', 'id_client']
    success_url = '/feedback/'


def c_last_month(request):
    clm = {}
    try:
        first_day = datetime.date.today().replace(day=1)
        last_day = first_day - datetime.timedelta(days=1)
        clm['clients'] = Bill.objects.all().filter(date_checkout__lte=str(last_day),
                                                   date_checkin__gte=str(last_day.replace(day=1)))
    except Bill.DoesNotExist:
        raise Http404("No clients ordered a room last month")
    return render(request, 'clm.html', clm)
