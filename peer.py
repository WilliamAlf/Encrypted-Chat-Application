from communcations import Listener, Sender


class Peer:
    receiver_ip = ""
    port = 5025

    def __init__(self):
        self.sender = Sender(self.receiver_ip, self.port, self)
        self.listener = Listener(self.port, self)

    def connect_to_chat(self):
        self.sender.start_connection_thread()
        self.listener.wait_for_client_to_connect()

    def send_message(self, message):
        try:
            self.sender.send_message(message)
            print("[SEND SUCCESS] Message was sent and received")

        except ConnectionRefusedError:
            print("[SEND ERROR] Message was sent but not received")

        except Exception as e:
            print("[SEND ERROR] Failed to send message", e)

    def leave_chat(self):
        self.listener.close_socket()
        self.sender.close_socket()

    def listen_for_public_key(self):
        return self.listener.listen_for_public_key()

    def start_listener(self):
        self.listener.start_listener()

