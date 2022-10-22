import rsa


class Encryption:

    def __init__(self):
        self.pubkey, self.privkey = rsa.newkeys(512)

    def recive_pubkey(self, pub_key):
        self.recieved_pubkey = pub_key

    def send_pubkey(self):
        return self.pubkey

    def encryption(self, MESSAGE):
        MESSAGE = MESSAGE.encode('utf-8')
        single_key = rsa.encrypt(MESSAGE, self.privkey)  # TODO: rsa.encrypt fungerar ej med privkey
        double_key = rsa.encrypt(single_key, self.recieved_pubkey)
        return double_key

    def decryption(self, MESSAGE):
        print(MESSAGE.decrypt(MESSAGE, self.privkey))
