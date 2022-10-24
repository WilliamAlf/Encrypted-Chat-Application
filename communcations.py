import socket
from threading import Thread


class Listener:
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener_thread = None
    has_connection = False
    client = None
    address = None

    def __init__(self, port, peer):
        self.peer = peer
        self.socket.bind(("", port))
        self.socket.listen()
        self.saved_message = None

    def wait_for_client_to_connect(self):
        if not self.has_connection:
            print("[CONNECTING_L] Waiting for client to connect")

            self.client, self.address = self.socket.accept()  # Blocker

            print(f"[CONNECTED_L] Client {self.address} has connected")
            self.connection_found()

    def connection_found(self):
        self.has_connection = True

        if not self.peer.sender.has_connection:
            self.peer.sender.connect_to_client()
        # Moved start_listener method call to main file to allow encryption key send/receive

    def start_listener(self):
        self.listener_thread = Thread(target=self.listen_for_message)
        self.listener_thread.start()

    def listen_for_public_key(self):
        return self.client.recv(1024).decode("utf-8")

    def listen_for_message(self):
        while True:
            received_message = self.client.recv(1024)

            if received_message == "quit":
                print("[END] Client left the chat")
                self.peer.leave_chat()
                break
            elif received_message:
                print(f"[MESSAGE RECEIVED] - {received_message}")
                self.saved_message = received_message

            elif not received_message:
                print("[END] Client has disconnected")
                self.peer.leave_chat()
                break

    def reset_saved_message(self):
        self.saved_message = None

    def close_socket(self):
        self.socket.close()


class Sender:
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    has_connection = False
    connection_thread = None

    def __init__(self, ip, port, peer):
        self.receiver_ip = ip
        self.port = port
        self.peer = peer

    def start_connection_thread(self):
        self.connection_thread = Thread(target=self.connect_to_client)
        self.connection_thread.start()

    def connect_to_client(self):
        connection_success, connection_fail = (True, False)
        if not self.has_connection:
            try:
                print("[CONNECTING_S] Connecting to client")
                self.socket.connect((self.receiver_ip, self.port))

            except (TimeoutError, ConnectionRefusedError, OSError):
                print("[CONNECTING_S] Client is offline, standing by")

            else:
                print(f"[CONNECTED_S] You have connected to {self.receiver_ip}")
                self.has_connection = connection_success

            finally:
                self.has_connection = connection_fail

    def send_message(self, message):
        self.socket.sendall(message)

    def close_socket(self):
        self.socket.close()
