import socket
import threading

"""
class Listener:
    pass

class Sender:
    pass
"""

HOST = "127.0.0.1"  # Make sure IP i correct
PORT = 5050

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
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
            conn.sendall(data)
