import bs4
import json
import random
import requests

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class RoomConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'room_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'status': text_data_json['status'],
                'name': text_data_json['name'],
            }
        )

    def chat_message(self, event):
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'status': event['status'],
            'name': event['name']
        }))


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        type = 'text' if not 'type' in text_data_json else text_data_json['type']
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message_type': type,
                'message': message
            }
        )

    def chat_message(self, event):
        message = event['message']
        type = event['message_type']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message_type': type,
            'message': message
        }))


class TasksConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'tasks_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        subject = text_data_json['subject']
        grade = text_data_json['grade']

        tasks = self.get_tasks(subject, grade)

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'subject': subject,
                'grade': grade,
                'tasks': tasks,
            }
        )

    def chat_message(self, event):
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'tasks': event['tasks'],
            'subject': event['subject'],
            'grade': event['grade'],
        }))

    SUBJECTS_GRADES_IDS = {
        'math': {
            '11': [35853705, 35517054],
        },
        'inf': {
            '11': [7896334, 7896336],
        },
        'rus': {
            '11': [20813643, 20813656]
        },
        'bio': {
            '11': [4049797, 4049798]
        }
    }

    def get_tasks(self, subject, grade):
        test_ids = self.SUBJECTS_GRADES_IDS[subject][grade]

        url = 'https://%s-ege.sdamgia.ru/test?id=%s&nt=True&pub=False'
        r = requests.get(url % (subject, random.choice(test_ids)))
        soup = bs4.BeautifulSoup(r.content)
        c = soup.find_all('div', {'class': 'prob_view'})[1]

        html = ''

        for c in soup.find_all('div', {'class': 'prob_view'}):
            html += str(c).replace('src="/', 'src="https://ege.sdamgia.ru/')

        return html


class BoardConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'board_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'x': text_data_json['x'],
                'y': text_data_json['y'],
                'x0': text_data_json['x0'],
                'y0': text_data_json['y0'],
            }
        )

    def chat_message(self, event):
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'x': event['x'],
            'y': event['y'],
            'x0': event['x0'],
            'y0': event['y0'],
        }))
