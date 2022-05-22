import logging
import threading
from typing import Tuple

import socket

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())


class BaseServer:
    BUFFER_SIZE = 2 ** 14

    def __init__(self, address: str, port: int) -> None:
        self.address = address
        self.port = port
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.conn.bind((self.address, self.port))
        self.conn.settimeout(60)

    def _client_handler(self, client_socket: socket.socket, address: Tuple[str, int]) -> None:
        while True:
            try:
                try:
                    message = self._recv_data(client_socket)
                except OSError:
                    break

                if not message:
                    break

                self._handle(client_socket, address, message)
                break
            except (KeyboardInterrupt, socket.timeout) as e:
                break
            except Exception as e:
                if client_socket:
                    self._send_message(client_socket, repr(e))
                    break

        self._close_client(client_socket, address)

    def _recv_data(self, client_socket: socket.socket) -> str:
        data = client_socket.recv(self.BUFFER_SIZE)
        udata = data.decode('utf-8')
        return udata

    def _prepare_data(self, data: str):
        raise NotImplemented()

    def _handle(self, client_socket: socket.socket, address: Tuple[str, int], data: str) -> None:
        raise NotImplemented()

    def _close_client(self, client_socket: socket.socket, address: Tuple[str, int]) -> None:
        client_socket.close()

    def _close_connection(self) -> None:
        self.conn.shutdown(socket.SHUT_RDWR)
        self.conn.close()

    def _send_message(self, client_socket: socket.socket, message: str) -> None:
        logger.info('Отправляется сообщение: %s', message)

        while True:
            sent_len = client_socket.send(message.encode('utf-8'))
            if sent_len == len(message):
                break
            message = message[sent_len:]

    def loop(self) -> None:
        logger.info(f'Сервер: адрес = {self.address}, порт = {self.port}')
        self.conn.listen(10)

        try:
            while True:
                client_socket, address = self.conn.accept()
                logger.info("Новое соединение {}".format(address))
                client_thread = threading.Thread(
                    target=self._client_handler,
                    args=(client_socket, address)
                )
                client_thread.daemon = True
                client_thread.start()
        except KeyboardInterrupt:
            logger.info("Выключаемся...")
        except Exception as e:
            print(e)
            self._close_connection()
