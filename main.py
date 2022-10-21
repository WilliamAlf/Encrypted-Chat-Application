from userInterface import Window
from peer import Peer


def start_chat():
    #   window.run()
    peer.connect_to_chat()

    while True:
        message = input("Enter your message: ")

        if message == "quit":
            peer.leave_chat()
            break

        else:
            peer.send_message(message)


if __name__ == "__main__":
    window = Window()
    peer = Peer()

    start_chat()

    
