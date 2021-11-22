from django.shortcuts import render

from django.http import Http404
from django.shortcuts import render
from simple_django_web_project.djangoApp.models import CarOwner


def owner(request, CarOwner_id):
    try:
        p = CarOwner.objects.get(pk=CarOwner_id)
    except CarOwner.DoesNotExist:
        raise Http404("CarOwner does not exist")
    return render(request, 'owner.html', {'owner': p})
