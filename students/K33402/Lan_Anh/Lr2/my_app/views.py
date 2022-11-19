from django.http import Http404
from django.shortcuts import render
from .models import Room, Bill, Comment, Client, Hotel
from .forms import *
import datetime
from django.views.generic.edit import UpdateView, DeleteView



def detail(request, id):
    p = {}
    try:
        p['dataset'] = Room.objects.get(pk = id)
    except Room.DoesNotExist:
        raise Http404("Room does not exist")
    return render(request, 'Room.html', p)

def detail1(request):
    q = {}
    try:
        q['dataset'] = Room.objects.all()
    except Room.DoesNotExist:
        raise Http404("Room does not exist")
    return render(request, 'Room1.html', q)

def detail2(request, id):
    p = {}
    try:
        p['dataset'] = Client.objects.get(pk = id)
    except Client.DoesNotExist:
        raise Http404("Client does not exist")
    return render(request, 'Client.html', p)

def detail3(request):
    q = {}
    try:
        q['dataset'] = Client.objects.all()
    except Client.DoesNotExist:
        raise Http404("Client does not exist")
    return render(request, 'Client1.html', q)

def create_bill(request):
    context = {}
    form = create_bill1(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_bill.html", context)

def create_client(request):
    context = {}
    form1 = create_client1(request.POST or None)
    if form1.is_valid():
        form1.save()
    context['form'] = form1
    return render(request, "create_client.html", context)

def create_comment(request):
    context = {}
    form = create_commnent1(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_comment.html", context)

def detail4(request):
    q = {}
    try:
        q['dataset'] = Bill.objects.all()
    except Bill.DoesNotExist:
        raise Http404("Bill does not exist")
    return render(request, 'Bill1.html', q)

class BillUpdateView(UpdateView):
    model = Bill
    template_name = 'update_bill.html'
    fields = ['Date', 'Check_in', 'Check_out', 'id_client', 'id_room']
    success_url = '/Bill/'

class BillDeleteView(DeleteView):
    model = Bill
    template_name = 'bill_confirm_delete.html'
    success_url = '/Bill/'

def detail5(request):
    q = {}
    try:
        today = datetime.date.today()
        first_day = today.replace(day=1)
        last_day = first_day - datetime.timedelta(days=1)
        q['dataset'] = Bill.objects.all().filter(Check_out__lte=str(last_day),
                                            Check_in__gte=str(last_day.replace(day=1)))
    except Bill.DoesNotExist:
        raise Http404("Bill does not exist")
    return render(request, 'Bill2.html', q)
