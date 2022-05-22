import socket
import os
import sys

if sys.path[0].endswith('2_html'):
    sys.path[0] = sys.path[0][:-7]

from typing import Tuple, Union

from base import BaseServer
from db import get_db

BASE_DIR = os.path.dirname(__file__)
db = next(get_db()) 


def subjects_to_html(subjects):
    return "\n".join(list(map(
        lambda subject: f"""
            <li class="list-group-item d-flex justify-content-between align-items-start">
                <div class="ms-2 me-auto">
                <div class="fw-bold">{subject['name']}</div>
                    Grade: {subject['grade']}
                </div>
            </li>
        """,
        subjects
    )))


class Response:
    RESPONSES_DESCRIPTION = {
        200: "OK",
        404: "FORBIDDEN",
        400: "BAD REQUEST",
    }

    def __init__(self, value: dict, method: str = 'GET', status: int = 200) -> None:
        self.value = value
        self.status = status

    def get_status_description(self) -> str:
        return self.RESPONSES_DESCRIPTION[self.status]

    def __str__(self):
        pass


class HTMLRender:
    def __init__(self):
        self.templates_dir = os.path.join(BASE_DIR, 'templates')

    def render(self, template_name: str, data: dict) -> str:
        filepath = os.path.join(self.templates_dir, template_name)

        with open(filepath, 'r') as f:
            rendered = f.read().format(**data)

        return rendered


class HTMLResponse(Response):
    def __init__(self, template_name: str, value: dict, status: int = 200) -> None:
        self.template_name = template_name
        self.renderer = HTMLRender()
        super(HTMLResponse, self).__init__(value, status)

    def get_status(self):
        return f"HTTP/1.1 {self.status} {self.get_status_description()}"

    def get_header(self, html):
        import datetime
        current_date = datetime.datetime.now().strftime('%a, %d %h %Y %H:%M%S')
        
        return f"Date: {current_date} GMT\r\nServer: Python socket\r\nContent-Length: {len(html)}\r\nContent-Type: text/html; charset=UTF-8\r\nKeep-Alive: timeout=5, max=1000\r\nConnection: Keep-Alive"

    def get_body(self, html):
        return f"{html}"

    def __str__(self):
        html = self.renderer.render(self.template_name, self.value)
        
        status = self.get_status()
        header = self.get_header(html)
        body = self.get_body(html)
        
        return f"{status}\r\n{header}\r\n\r\n{body}\r\n"


class HTTP1Parser:
    def parse_headers(self, udata: str) -> dict:
        first_line = udata.split('\n')[0]
        method, path, http_version = first_line.split()

        return {
            'method': method,
            'url': path,
            'http_version': http_version,
        }

    def parse_post(self, udata: str) -> dict:
        params = udata.split('\r\n\r\n')[1]

        return {
            param: key
            for param, key in list(map(
                lambda x: x.split('='),
                params.split('&')
            ))
        }

    def parse(self, response: Response) -> dict:
        udata = str(response)
        data = {}
        data.update(self.parse_headers(udata))

        if data['method'] == 'POST':
            data.update(self.parse_post(udata))

        return data


class TasksServer(BaseServer):
    def __init__(self, *args, **kwargs):
        super(TasksServer, self).__init__(*args, **kwargs)
        self.parser = HTTP1Parser()

    def _recv_data(self, client_socket: socket.socket) -> dict:
        udata = super(TasksServer, self)._recv_data(client_socket)
        if not udata:
            return

        data = self.parser.parse(udata)
        return data

    def _send_message(self, client_socket: socket.socket, message: Union[str, Response]) -> None:
        if isinstance(message, str):
            return self._send_message(
                client_socket, 
                HTMLResponse('bad.html', {'message': message})
            )

        message = str(message)
        super(TasksServer, self)._send_message(client_socket, message)

    def _handle(self, client_socket: socket.socket, address: Tuple[str, int], data: dict) -> None:
        method = data['method']
        
        handler_name = '_%s_method' % method
        handler = getattr(self, handler_name, None)
        if not handler:
            raise ValueError("Обработчика запросов вида %s нет." % method)

        # TODO: добавить обработку по path
        response = handler(data)
        self._send_message(client_socket, response)

    def _GET_method(self, data: dict) -> None:
        subjects = list(db.all())
        return HTMLResponse('subjects.html', {'subjects': subjects_to_html(subjects)})

    def _POST_method(self, data: dict) -> None:
        error_message = ''
        grade = data['grade']

        if not grade.isdigit():
            error_message = "Неверный формат оценки"
        elif 0 < int(data['grade']) <= 5:
            db.create(data['subject_name'], {'name': data['subject_name'], 'grade': data['grade']})
        else:
            error_message = "Оценка должна быть в интервале (0, 5]"

        subjects = list(db.all())

        return HTMLResponse('subjects.html', {
            'subjects': subjects_to_html(subjects), 
            'error_message': error_message
        })


if __name__ == "__main__":
    server = TasksServer(address="127.0.0.1", port=8100)
    server.loop()
