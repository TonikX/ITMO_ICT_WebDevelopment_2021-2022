from django.contrib.auth import base_user
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.views import View
from django.contrib import messages
from .models import Race, User, RacerRegistration, RacerProfile, Comment, Commentator
from .forms import CommentForm, CustomUserCreationForm, CustomRacerCreationForm, RaceEditRegistrationForm, \
    RaceRegistrationForm
from django.contrib.auth import authenticate, login


# Create your views here.
def index(request):
    return render(request, 'race_winners/index.html')


def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            usr = f.save()
            login(request=request, user=usr)
            if usr.user_type == 1:
                print("here")
                return redirect('racer_reg')
            else:
                commentatorProfile = Commentator.objects.create(
                    user_info=usr,
                    raiting=1
                )
                commentatorProfile.save()
                return redirect('/')

    else:
        f = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': f})


def racer(request):
    if request.method == 'POST':
        f = CustomRacerCreationForm(request.POST, user=request.user)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('/')
    else:
        f = CustomRacerCreationForm(user=request.user)

    return render(request, 'registration/racer.html', {'form': f})


class RaceListView(ListView):
    model = Race


class RaceDetailView(DetailView):
    model = Race

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        racer_regs = RacerRegistration.objects.filter(race=context['object']).all()
        context['racer_regs'] = racer_regs

        if self.request.user.is_authenticated:
            if self.request.user.user_type == 1:
                context['is_racer'] = True
                if (racer_regs.filter(racer=RacerProfile.objects.get(base_user=self.request.user))).exists():
                    context['in_race'] = True
                else:
                    context['in_race'] = False
            else:
                context['is_racer'] = False
                commentator = Commentator.objects.get(user_info=self.request.user)
                context['comment_form'] = CommentForm(self.request.POST, commentator=commentator,
                                                      race=context['object'])

        commets = Comment.objects.filter(race=context['object']).all()
        context['comments'] = commets
        return context


def profile(request):
    context = dict()
    if request.method == 'GET':
        if request.user.user_type == 1:
            racer = RacerProfile.objects.get(base_user=request.user)
            context['is_racer'] = 1
            context['racer'] = racer
            racer_reg_list = RacerRegistration.objects.filter(racer=racer).all()
            race_list = [racer_reg.race for racer_reg in racer_reg_list]
            context['race_list'] = race_list

    return render(request, 'registration/profile.html', context=context)


def race_register_add(request, race_id):
    race = Race.objects.get(pk=race_id)
    if request.method == 'POST':
        f = RaceRegistrationForm(request.POST, racer=RacerProfile.objects.get(base_user=request.user), race=race)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('/')
    else:
        f = RaceRegistrationForm(racer=RacerProfile.objects.get(base_user=request.user), race=race)

    return render(request, 'race_winners/race_registration.html', {'form': f})


def race_leave(request, race_id):
    race = Race.objects.get(pk=race_id)
    if (RacerRegistration.objects.filter(race=race, racer=RacerProfile.objects.get(base_user=request.user)).exists()):
        RacerRegistration.objects.filter(race=race, racer=RacerProfile.objects.get(base_user=request.user)).delete()
        return redirect('/race_list')
    else:
        return HttpResponse("Error")


def race_register_edit(request, race_id):
    race = Race.objects.get(pk=race_id)
    race_reg = RacerRegistration.objects.get(race=race, racer=RacerProfile.objects.get(base_user=request.user))
    if request.method == 'POST':
        f = RaceEditRegistrationForm(request.POST, race_reg=race_reg, initial={'car': race_reg.car})
        if f.is_valid():
            f.save()
            messages.success(request, 'Edited successfully!')
            return redirect('/')
        else:
            print("Invalid")
    else:
        f = RaceEditRegistrationForm(race_reg=race_reg, initial={'car': race_reg.car})

    return render(request, 'race_winners/race_registration_edit.html', {'form': f})


def add_commet(request, race_id):
    commentator = Commentator.objects.get(user_info=request.user)
    race = Race.objects.get(pk=race_id)
    if request.method == 'POST':
        f = CommentForm(request.POST, commentator=commentator, race=race)
        if f.is_valid():
            f.save()
            messages.success(request, 'Edited successfully!')
            return redirect("/race/{}".format(race_id))
        else:
            print("Invalid")