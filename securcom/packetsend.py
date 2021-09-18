import socket
# import aes
# import passwd

# class Packet(object):
#     def __init__(self, message, pseudo):
#         self.message = str(message)
#         self.pseudo = str(pseudo)


# encrypt = aes.AESCipher(passwd.passwd_var).encrypt(message)

def send():
    ip, port = ('', 6666)
    send_var = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        send_var.connect((ip, port))
    except ConnectionRefusedError:
        print("Le server de reception n'est pas demarer")
    except:
        print("une erreur est survenu")
    finally:
        send_var.close()



















