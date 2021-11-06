import random

import bs4
import requests

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from room.models import Room


@login_required
def room_list(request):
    subject = request.GET.get('subject', '')
    subject_rooms = Room.objects.filter(subject__icontains=subject).order_by('-pub_date')

    paginator = Paginator(subject_rooms, 10)
    page_number = request.GET.get('page', 1)
    room_list = paginator.get_page(page_number)
    subjects = Room.SUBJECTS

    return render(request, 'room/room-list.html', locals())


@login_required
def room(request, id):
    room = Room.objects.get(id=id)
    return render(request, 'room/group-room.html', locals())


@login_required
def create_room(request):
    room_name = 'create_room'
    subjects = Room.SUBJECTS

    if request.method == "POST":
        room_name = request.POST.get('room-name')
        room_subject = request.POST.get('room-subject')
        room_description = request.POST.get('room-description', '')

        room = Room.objects.create(
            name=room_name,
            subject=room_subject,
            description=room_description,
            audio_works='room-audio-works' in request.POST,
            creator=request.user.username)

        return redirect(reverse_lazy('room', kwargs={'id': room.id}))

    return render(request, 'room/create-room.html', locals())
