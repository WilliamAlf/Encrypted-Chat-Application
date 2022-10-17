import socket
from threading import Thread

HOST = "127.0.0.1"  # Make sure IP i correct
LISTENER_PORT = 5050
TALKING_PORT = 9090


def listen():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, LISTENER_PORT))
        s.listen()
        # conn - socket object representing the connection; addr - tuple holding address of client
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"{data}")


def send(message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, TALKING_PORT))
        s.sendall(message.encode(encoding="UTF-8"))
        data = s.recv(1024)

    print(f"Received {data!r}")


if __name__ == "__main__":
    listenerThread = Thread(target=listen, args=())
    listenerThread.start()

    user1 = Thread(target=send, args=("Hello1", ))
    user1.start()





