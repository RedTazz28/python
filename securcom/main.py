import packetsend

pseudo = input("ton pseudo")

message = input("entez votre message : ")

packetsend.Packet.send(message=message)