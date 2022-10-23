import rsa


class Encryption:

    def __init__(self):
        self.pubkey, self.privkey = rsa.newkeys(512)
        self.received_pubkey = None

    def construct_received_pubkey(self, indata):
        n, e = tuple(indata.split(' '))

        self.received_pubkey = rsa.PublicKey(int(n), int(e))

    def encryption(self, MESSAGE):
        MESSAGE = MESSAGE.encode('utf-8')
        single_key = rsa.encrypt(MESSAGE, self.received_pubkey)
        return single_key

    def decryption(self, MESSAGE):
        print(MESSAGE.decrypt(MESSAGE, self.privkey))
