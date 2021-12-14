from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from rooms.models import Room


class RoomListView(LoginRequiredMixin, ListView):
    model = Room
    template_name = 'list_rooms.html'


class RoomDetailView(LoginRequiredMixin, DetailView):
    model = Room
    template_name = 'view_room.html'

    def get_context_data(self, **kwargs):
        # Fetch comments for room
        context = super(RoomDetailView, self).get_context_data(**kwargs)
        comments = []
        for booking in self.get_object().bookings.all():
            if hasattr(booking, 'comment'):
                comments.append(booking.comment)
        context['comments'] = comments
        return context
