from django.http import Http404, HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
# from app.forms import OwnerForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from app.models import Owner, Car
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
