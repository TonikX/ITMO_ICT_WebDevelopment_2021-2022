from django.shortcuts import render

# Create your views here.

from django.http import Http404
from cars.models import Car_owner

def car_owner_info(request, car_owner_id):
    try:
        o = Car_owner.objects.get(pk=car_owner_id)
    except Car_owner.DoesNotExist:
        raise Http404("Car owner does not exist")
    return render(request, 'cars/owner.html', {'car_owner': o})
