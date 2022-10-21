from communcations import Listener, Sender


class Peer:
    responder_ip = "localhost"
    port = 5024

    def __init__(self, send_port, listen_port):
        self.sender = Sender(self.responder_ip, send_port, self)
        self.listener = Listener(listen_port, self)

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
        print("[END] You left the chat")
        self.listener.close_socket()
        self.sender.close_socket()

