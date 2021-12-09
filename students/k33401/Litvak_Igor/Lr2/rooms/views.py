from django.views.generic import ListView, DetailView
from rooms.models import Room


class RoomListView(ListView):
    model = Room
    template_name = 'list_rooms.html'


class RoomDetailView(DetailView):
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
