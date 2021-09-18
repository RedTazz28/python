import socket
import aes
import passwd

class Packet():
    def __init__(self, mesage):
        self.message = mesage

    def send(self, message):
        encrypt = aes.AESCipher(passwd.passwd_var).encrypt(message)
        

    def receive(self, message):
        decrypte = aes.AESCipher(passwd.passwd_var).decrypt(message)





