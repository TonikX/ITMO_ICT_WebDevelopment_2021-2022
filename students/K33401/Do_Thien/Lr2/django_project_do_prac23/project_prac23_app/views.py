# from django.db.models import query
from django.http import Http404
from django.http.response import HttpResponse
from django.shortcuts import render
# from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
# from django.views.generic.edit import CreateView, UpdateView
# from django.views.generic.edit import DeleteView


from .models import OwnerUser
from .forms import ExampleForm
import datetime


def detail(request):
    try:
        context = {}
        context["dataset"] = OwnerUser.objects.all()
    except:
        raise Http404("Owner doesn't exist")
    return render(request, 'owner.html', context)


def detail_view(request, id):
    context2 = {}
    context2["data"] = OwnerUser.objects.get(id = id)
    return render(request, "detail_view.html", context2)
  
def CreateView(request):
    context3 ={}
    form = ExampleForm(request.POST or None) 
    if form.is_valid(): 
        form.save()
    context3['form'] = form
    return render(request, "create_view.html", context3)

def TimeView(request):
    now = datetime.datetime.now()
    html = "Time is {}".format(now)
    return HttpResponse(html)

