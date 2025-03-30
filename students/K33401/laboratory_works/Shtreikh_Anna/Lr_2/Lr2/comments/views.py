from django.shortcuts import render, get_object_or_404

from hotels.models import Room,Hotel
from .models import *
from .forms import *

def comments(request, h_id, r_id):
    room = get_object_or_404(Room, id=r_id)
    comments = Comment.objects.filter(room=room)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            com = form.save(commit=False)
            com.user = request.user
            com.room = room
            com.save()
            form = CommentForm()
    else:
        form = CommentForm()
    return render(request, "comments.html",
                  {"room": room,
                   "comments": comments,
                   "form": form})
