from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView
from .models import *
from .forms import *
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used!')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords dont match')
            return redirect('register')

    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'User doesnt exists')
            return redirect('login')
    else:
        return render(request, 'login.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')


def rooms(request):
    free_rooms = Room.objects.filter(is_reserved=False).order_by('-number')
    return render(request, 'rooms.html', {'rooms': free_rooms})


def room(request, pk):
    room = Room.objects.get(id=pk)
    comments = Comment.objects.filter(room=room)
    return render(request, 'room.html', {'room': room, 'comments': comments})


@login_required
def reservation(request, pk):
    obj = get_object_or_404(Room, id=pk)
    user = request.user
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form['arrival_date'].value() != form['departure_date'].value():
            if form.is_valid():
                res = form.save(commit=False)
                res.user = user
                obj.is_reserved = True
                res.room = obj
                obj.save()
                res.save()
                return redirect('/')
        else:
            messages.info(request, 'Arrival and departure date are equal')
    else:
        form = ReservationForm()
    return render(request, 'reservation.html', {'form': form, 'room': obj})


@login_required
def profile(request):
    user = request.user
    reservations = Reservation.objects.all().order_by('-reserve_time')
    return render(request, 'profile.html', {'reservations': reservations, 'user': user})


@login_required
def delete_reservation(request, pk):
    obj = get_object_or_404(Reservation, id=pk)
    room = obj.room
    room.is_reserved = False
    room.save()
    obj.delete()
    return redirect('/profile')


@login_required
def edit_reservation(request, pk):
    obj = get_object_or_404(Reservation, id=pk)
    room = obj.room
    form = ReservationForm(request.POST or None, instance=obj)
    if form['arrival_date'].value() != form['departure_date'].value():
        if form.is_valid():
            res = form.save(commit=False)
            res.reserve_time = datetime.now()
            res.save()
            return redirect('/profile')
    else:
        messages.info(request, 'Arrival and departure date are equal')

    return render(request, 'reservation.html', {'form': form, 'room': room})


@login_required
def add_comment(request, pk):
    obj = get_object_or_404(Room, id=pk)
    user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form['text'].value():
            if form['rate'].value():
                if form.is_valid():
                    com = form.save(commit=False)
                    com.user = user
                    com.room = obj
                    com.save()
                    return redirect('/rooms')
            else:
                messages.info(request, 'You must rate the room!')
        else:
            messages.info(request, 'You should type something!')
    else:
        form = CommentForm()
    return render(request, 'comment.html', {'form': form})


@login_required
def show_last_month(request):
    obj = Reservation.objects.filter(departure_date__gt=datetime.now() - timedelta(days=30))
    print(datetime.now() - timedelta(30))
    return render(request, 'lastmonth.html', {'objects': obj})
