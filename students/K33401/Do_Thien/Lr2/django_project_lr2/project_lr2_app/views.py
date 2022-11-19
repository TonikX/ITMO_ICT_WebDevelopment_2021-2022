from django.shortcuts import render
from django.http import Http404
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from .models import User, Room
from .forms import *
import datetime



def RoomListView(request):
    try:
        context = {}
        context["dataset"] = Room.objects.all()
    except:
        raise Http404("Room doesn't exist")

    return render(request, 'room_list.html', context)

def DetailRoomView(request, id):
    context = {}
    context["data"] = Room.objects.get(id = id)

    return render(request, "detail_room.html", context)


def BookRoom(request):
    context ={}
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "book_room.html", context)


def UserListView(request):
    try:
        context = {}
        context["dataset"] = User.objects.all()
    except:
        raise Http404("User doesn't exist")

    return render(request, 'user_list.html', context)


def DetailUserView(request, id):
    context = {}
    context["data"] = User.objects.get(id = id)

    return render(request, "detail_user.html", context)


def CreateUser(request):
    context ={}
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_user.html", context)


def BillListView(request):
    try:
        context = {}
        context["dataset"] = Bill.objects.all()
    except:
        raise Http404("Room doesn't exist")

    return render(request, 'bill_list.html', context)


class UpdateBill(UpdateView):
    model = Bill
    template_name = 'bill_update.html'
    fields = ['time', 'date_start', 'check_in', 'check_out', 'id_room', 'id_user']
    success_url = '/bill/'


class DeleteBill(DeleteView):
  model = Bill
  template_name = 'bill_delete.html'
  success_url = '/bill/'


def Comment(request):
    context ={}
    form = CommnetForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "comment.html", context)


def ListUserLastMonth(request):
    context = {}
    try:
        today = datetime.date.today()
        first_day = today.replace(day=1)
        last_day = first_day - datetime.timedelta(days=1)
        print(str(last_day))
        context['dataset'] = Bill.objects.all().filter(check_out__lte=str(last_day), check_in__gte=str(last_day.replace(day=1)))
    except Bill.DoesNotExist:
        raise Http404("There is not any clients last month.")
    return render(request, 'user_last_month.html', context)