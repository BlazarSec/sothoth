import threading
import socket

from select import select

def serv_handle(serv_sock, event):
    serv_sock.listen(5)
    pool = [serv_sock]

    while not event.is_set():
        for r, _, _ in select(pool, [], []):
            if r is serv_sock:
                pool.append(r.accept()[0])
                continue

class Server():
    def __init__(self, bind_addr, bind_port=80):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("localhost", bind_port))

        self.serv_sock = sock
        self.serv_event = threading.Event()
        self.serv_thread = None

    # start inbound connection handler
    def start(self):
        if self.serv_thread is not None:
            raise ValueError("Server.start method called from already running server")

        self.serv_event.clear()
        self.serv_thread = threading.Thread(target=serv_handle, args=(self.serv_sock, self.serv_event))
        self.serv_thread.start()

    # stop inbound connections and wait for living threads to die.
    def stop(self):
        if self.serv_thread is None:
            raise ValueError("Server.stop method called from already stopped server")