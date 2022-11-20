from django.urls import re_path
from django.conf import settings

from . import consumers


websocket_urlpatterns = [
    re_path(r'^ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'^ws/tasks/(?P<room_name>\w+)/$', consumers.TasksConsumer.as_asgi()),
    re_path(r'^ws/board/(?P<room_name>\w+)/$', consumers.BoardConsumer.as_asgi()),
]
