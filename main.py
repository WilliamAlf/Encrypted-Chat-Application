from userInterface import Window
from peer import Peer
from encryption import Encryption


def start_chat(window):
    # Startup and trading of encryption keys
    peer.connect_to_chat()

    enc = Encryption()

    peer.sender.send_message(f"{enc.pubkey.n} {enc.pubkey.e}".encode("utf-8"))
    enc.construct_received_pubkey(peer.listener.listen_for_public_key())

    # Start listener after encryption-key trade to avoid "racing the beam"
    peer.listener.start_listener()

    # Window run and mainloop
    window.run()
    while True:
        message = window.get_input()

        # Check for outgoing message and encrypt
        if message:
            if message == "quit":
                print("[END] You left the chat")
                peer.leave_chat()
                break

            else:
                peer.send_message(enc.encryption(message))
                window.reset_input()

        # Check for incoming message and decrypt
        if peer.listener.saved_message:
            window.receive_message(enc.decryption(peer.listener.saved_message))
            peer.listener.reset_saved_message()

        window.root.update_idletasks()
        window.root.update()


if __name__ == "__main__":
    window = Window()
    peer = Peer()

    start_chat(window)
