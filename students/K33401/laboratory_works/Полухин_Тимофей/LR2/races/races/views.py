from django.http.response import HttpResponseNotAllowed, HttpResponseRedirect, HttpResponseBadRequest
from django.views import generic
from .models import Race
from django import forms


class RacesView(generic.ListView):
    model = Race
    template_name = 'races/index.html'
    context_object_name = 'races'


class DetailView(generic.DetailView):
    model = Race
    template_name = 'races/race.html'
    context_object_name = 'race'


class ContactForm(forms.Form):
    race = forms.CharField(widget=forms.TextInput)


def register(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            race_id = form.cleaned_data['race']
            race = Race.objects.get(pk=race_id)
            race.racers.add(request.user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseBadRequest()
    else:
        return HttpResponseNotAllowed(permitted_methods=['POST'])


def unregister(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            race_id = form.cleaned_data['race']
            race = Race.objects.get(pk=race_id)
            race.racers.remove(request.user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseBadRequest()
    else:
        return HttpResponseNotAllowed(permitted_methods=['POST'])
