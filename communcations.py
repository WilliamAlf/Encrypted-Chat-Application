import socket
from threading import Thread


class Listener:
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener_thread = None
    has_connection = False
    client = None
    addr = None

    def __init__(self, port, peer):
        self.peer = peer
        self.socket.bind(("localhost", port))
        self.socket.listen()

    def wait_for_client_to_connect(self):
        if not self.has_connection:
            print("[CONNECTING_L] Waiting for client to connect")

            self.client, self.addr = self.socket.accept()  # Blocker

            print(f"[CONNECTED_L] Client {self.addr} has connected")
            self.connection_found()

    def connection_found(self):
        self.has_connection = True

        if not self.peer.sender.has_connection:
            self.peer.sender.connect_to_client()

        self.start_listener()

    def start_listener(self):
        self.listener_thread = Thread(target=self.listen_for_message)
        self.listener_thread.start()

    def listen_for_message(self):
        while True:
            received_message = self.client.recv(1024).decode("utf-8")

            if received_message == "quit":
                print("[END] Client left the chat")
                self.peer.leave_chat()
                break
            elif received_message:
                print(f"\n[MESSAGE RECEIVED] - {received_message}\nEnter your message: ")
            elif not received_message:
                print("[END] Client has disconnected")
                self.peer.leave_chat()
                break

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

            except (TimeoutError, ConnectionRefusedError) as e:
                print("[CONNECTING_S] Client is offline, standing by")

            else:
                print(f"[CONNECTED_S] You have connected to {self.receiver_ip}")
                return connection_success

            finally:
                return connection_fail

    def send_message(self, message):
        self.socket.sendall(message.encode("utf-8"))

    def close_socket(self):
        self.socket.close()