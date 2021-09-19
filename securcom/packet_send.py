import socket
import aes
import passwd
import datetime

# class Packet(object):
#     def __init__(self, message, pseudo):
#         self.message = str(message)
#         self.pseudo = str(pseudo)




def send(message, pseudo):
    encrypt = aes.AESCipher(passwd.passwd_var).encrypt(message)
    ip, port = ('127.0.0.1', 6665)
    send_var = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        send_var.connect((ip, port))
    except ConnectionRefusedError:
        print("Le server de reception n'est pas demarer")
    except:
        print("une erreur est survenu : verifier les ip")
    finally:
        pass




















