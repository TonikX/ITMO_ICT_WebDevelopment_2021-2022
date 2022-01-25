import socket
import logging
from base import BaseServer


logger = logging.getLogger(__name__)


class HelloWorldServer(BaseServer):

    def _handle(self, client_socket: socket.socket, address, data: str):
        print("Data: ", data)
        logger.info("data: %s", data)
        client_socket.send(b"Hello, Client")


if __name__ == "__main__":
    server = HelloWorldServer(address="127.0.0.1", port=8000)
    server.loop()
