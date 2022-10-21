import socket
from threading import Thread

HOST = "127.0.0.1"
PORT_LISTEN = 9090
PORT_SEND = 5050


def listen():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT_LISTEN))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                data = data.decode()
                if data == "QUIT":
                    print(f"[END] Client disconnected")
                    break
                elif data:
                    print(f"[MESSAGE RECEIVED] - {data}\n")


def send(message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT_SEND))
        s.sendall(message.encode("utf-8"))
        data = s.recv(1024)


if __name__ == "__main__":
    listenerThread = Thread(target=listen)
    listenerThread.start()

    while True:
        message = input("Enter your message: ")
        try:
            send(message)
            print("[MESSAGE RECEIVED] Message sent\n")
        except ConnectionRefusedError:
            print("[ERROR] Message not received\n")
        if message == "QUIT":
            break

    print("[END] You left the chat")

