import rsa


class Encryption:

    def __init__(self):
        self.pubkey, self.privkey = rsa.newkeys(512)
        self.received_pubkey = None

    def construct_received_pubkey(self, indata):
        n, e = tuple(indata.split(' '))

        self.received_pubkey = rsa.PublicKey(int(n), int(e))

    def encryption(self,  message):
        message = message.encode("utf-8")
        return rsa.encrypt(message, self.received_pubkey)

    def decryption(self, message):
        message = rsa.decrypt(message, self.privkey)
        return message.decode("utf-8")
