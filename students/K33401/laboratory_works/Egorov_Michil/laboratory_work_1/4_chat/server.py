from collections import defaultdict
from typing import Tuple
import logging
import socket

from base import BaseServer


logger = logging.getLogger(__name__)


class ChatServer(BaseServer):
    """
    :arg rooms: словарь где ключи - id комнат, а значения - множество адресов участников
    """
    clients_sockets = dict()
    clients_rooms = dict()
    rooms = defaultdict(set)

    def _prepare_data(self, data: str) -> dict:
        """ Передаем room_id и message
        Пример: room_id=1&message=привет,всем!
        """

        body = {}
        arguments = data.split('&')

        for argument in arguments:
            key, value = argument.split('=')
            body[key] = value

        return body

    def _change_client_room(self, address: Tuple[str, int], room_id: str) -> None:
        if address in self.clients_rooms and self.clients_rooms[address] == room_id:
            return

        self.rooms[room_id].discard(address)
        self.clients_rooms[address] = room_id
        self.rooms[room_id].add(address)

    def _close_client(self, client_socket: socket.socket, address: Tuple[str, int]) -> None:
        if address not in self.clients_rooms:
            return

        client_room_id = self.clients_rooms[address]
        self.rooms[client_room_id].discard(address)
        self.clients_rooms.pop(address)
        self.clients_sockets.pop(address)

        super()._close_client(client_socket, address)

    def _handle(self, client_socket: socket.SocketIO, address: Tuple[str, int], data: str) -> None:
        body = self._prepare_data(data)
        self.clients_sockets[address] = client_socket
        self._change_client_room(address, body['room_id'])
        for client_address in self.rooms[body['room_id']]:
            try:
                sock = self.clients_sockets[client_address]
                self._send_message(sock, body['message'])
            except Exception as e:
                logger.warning("Сообщение не отправилось: %s %s", client_address, repr(e))


if __name__ == "__main__":
    server = ChatServer("127.0.0.1", 8000)
    server.loop()
