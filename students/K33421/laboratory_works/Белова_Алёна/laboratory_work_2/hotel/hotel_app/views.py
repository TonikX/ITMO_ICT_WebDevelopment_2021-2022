from django.shortcuts import render
from django.http import Http404
from .models import Guest, Room, Accommodation
from .forms import GuestForm, AccommodationForm, CommentForm
from django.views.generic import UpdateView, DeleteView
import datetime


def guest_list(request):
    data = {"guests": Guest.objects.all()}
    return render(request, "guest_list.html", data)


def guest_create(request):
    data = {}
    form = GuestForm(request.POST or None)
    if form.is_valid():
        form.save()
    data["form"] = form
    return render(request, "guest_create.html", data)


def room_list(request):
    data = {"rooms": Room.objects.all()}
    return render(request, "room_list.html", data)


def book(request):
    data = {}
    form = AccommodationForm(request.POST or None)
    if form.is_valid():
        form.save()
    data["form"] = form
    return render(request, "book.html", data)


def comment(request):
    data = {}
    form = CommentForm(request.POST or None)
    if form.is_valid():
        form.save()
    data["form"] = form
    return render(request, "comment.html", data)


def last_month(request):
    data = {}
    try:
        month = datetime.date.today() - datetime.timedelta(days=31)
        data["accoms"] = Accommodation.objects.all().filter(check_in_date__gte=str(month),
                                                            check_out_date__lte=str(datetime.date.today()))
        print(data)
    except Accommodation.DoesNotExist:
        raise Http404("No guests this month yet :(")
    return render(request, "accom_list.html", data)


def accommodation_list(request):
    data = {"accoms": Accommodation.objects.all()}
    return render(request, "accom_list.html", data)


def home(request):
    return render(request, "home.html")


class AccomUpdate(UpdateView):
    model = Accommodation
    template_name = "accom_update.html"
    fields = ["check_in_date", "check_out_date", "guest", "room"]
    success_url = "/accom/list/"


class AccomDelete(DeleteView):
    model = Accommodation
    template_name = "accom_delete.html"
    success_url = "/accom/list/"


