import socket
from threading import Thread

# Choose appropriate port
# Port forward for WAN support

RECEIVER_IP = ""
PORT = 5024

LISTENER_SOCKET = None
SENDER_SOCKET = None

CONNECTED_TO_SENDER = False
CONNECTED_TO_CLIENT = False

#
"""class Listner:
    def __init__(self, PORT):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(("", PORT))

    def wait_for_client_to_connect():
        pass

    def listen_for_message():
        pass
class Sender:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_client():
        pass

    def client_connect_attempt():
        pass"""


# Receiving Socket
def open_listener_socket():
    global LISTENER_SOCKET

    if not LISTENER_SOCKET:
        LISTENER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        LISTENER_SOCKET.bind(("", PORT))

    LISTENER_SOCKET.listen()

    wait_for_client_to_connect()


def wait_for_client_to_connect():
    global CONNECTED_TO_SENDER
    global LISTENER_SOCKET

    print("[CONNECTING_L] Waiting for client to connect")

    if not CONNECTED_TO_SENDER:
        client, addr = LISTENER_SOCKET.accept()  # Blocker
        CONNECTED_TO_SENDER = True

    print(f"[CONNECTED_L] Client {addr} has connected")

    listener_thread = Thread(target=listen_for_message, args=(client,))
    listener_thread.start()

    connect_to_client()  # Second attempt now that client has connected to us (on main thread)


def listen_for_message(client):
    while True:
        received_message = client.recv(1024).decode("utf-8")

        if received_message == "quit":
            print("[END] Client left the chat")
            end_chat()
            break
        elif received_message:
            print(f"\n[MESSAGE RECEIVED] - {received_message}\nEnter your message: ")
        elif not received_message:
            print("[END] Client has disconnected")
            end_chat()
            break


# Sending Socket
def open_sending_socket():
    global SENDER_SOCKET

    if not SENDER_SOCKET:
        SENDER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    connect_to_client_initial_attempt = Thread(target=connect_to_client, args=(1,))
    connect_to_client_initial_attempt.start()


def connect_to_client(attempts=1):
    global CONNECTED_TO_CLIENT

    if not CONNECTED_TO_CLIENT:
        print(f"[CONNECTING_S] Trying to connect to {RECEIVER_IP}")

        for attempt in range(attempts):
            if CONNECTED_TO_CLIENT:
                return
            CONNECTED_TO_CLIENT = client_connect_attempt(attempt, attempts)


def client_connect_attempt(attempt, attempts):
    global SENDER_SOCKET

    connection_success, connection_fail = (True, False)

    try:
        SENDER_SOCKET.connect((RECEIVER_IP, PORT))

    except (TimeoutError, ConnectionRefusedError) as e:
        if attempt == 0:
            print("[CONNECTING_S] Client is offline")

        if attempt == attempts - 1:
            print("[CONNECTING_S] Standing by")

    else:
        print(f"[CONNECTED_S] You have connected to {RECEIVER_IP}")
        return connection_success

    finally:
        return connection_fail


# App Functions
def initiate_connections():
    open_sending_socket()
    open_listener_socket()


def start_chat():
    initiate_connections()

    while True:
        message = input("Enter your message: ")

        if message == "quit":
            end_chat()
            break

        else:
            try:
                send_message(message)
                print("[SEND SUCCESS] Message was sent and received")

            except ConnectionRefusedError:
                print("[SEND ERROR] Message was sent but not received")

            except Exception as e:
                print("[SEND ERROR] Failed to send message", e)


def send_message(message):
    SENDER_SOCKET.sendall(message.encode("utf-8"))


def end_chat():
    global LISTENER_SOCKET
    global SENDER_SOCKET

    LISTENER_SOCKET.close()
    SENDER_SOCKET.close()

    print("[END] You left the chat")


if __name__ == "__main__":
    start_chat()

