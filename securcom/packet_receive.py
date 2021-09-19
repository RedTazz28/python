import socket
import passwd
import aes

def receive():
    message = "test"
    print("Vous etes en ligne UP")
    host, host_port = ('127.0.0.1', 6665)
    receive_var = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    receive_var.bind((host, host_port))
    while True:
        receive_var.listen()
        conn, address = receive_var.accept()
        print("un client is up : {}")
        decrypte = aes.AESCipher(passwd.passwd_var).decrypt(message)



