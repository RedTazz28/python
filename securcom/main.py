import packet_send as ps
import packet_receive as pr

pr.receive()

pseudo = "Ping"

while True:
    message = input("Message : ")
    message_len = len(message)
    if message_len <= 1:
        print("Message trop cour")
        continue
    else:
        ps.send(message, pseudo)
        continue




