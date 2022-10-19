import socket
from threading import Thread

RECEIVING_CLIENT = "192.168.1.188"  # Make sure IP is correct
LISTENER_PORT = 9090
TALKING_PORT = 5050


def listener():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((RECEIVING_CLIENT, LISTENER_PORT))
        s.listen()
        # conn - socket object representing the connection; addr - tuple holding address of client
        conn, addr = s.accept()
        print(f"Connected by {addr}")
        with conn:
            while True:
                data = conn.recv(1024)
                data = data.decode("utf-8")
                if data == "QUIT":
                    return None
                elif data:
                    return f"[MESSAGE RECEIVED] - {data}"


def always_listen():
    """    online = True
        while online:
            received_message = listener()
            if received_message:
                print(received_message)
            else:
                print("[END OF CHAT] Receiving client has disconnected")
                online = False"""


def send(message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((RECEIVING_CLIENT, TALKING_PORT))
        s.sendall(message.encode(encoding="UTF-8"))
        data = s.recv(1024)

    print(f"Received {data!r}")


if __name__ == "__main__":
    listenerThread = Thread(target=listener, args=())
    listenerThread.start()

    run = True
    while run:
        message = input("Enter your message: ")
        try:
            send(message)
        except ConnectionRefusedError:
            print("[Error] Message not received")
        if message == "QUIT":
            run = False

