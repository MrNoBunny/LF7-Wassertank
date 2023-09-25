# Wichtige Bibliothek
import socket
#Socket erstellen
serverAddress = ('192.168.123.10' , 2222)
bufferSize = 1024
UDPClient = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
# Anfrage vom Client starten
msgFromClient ='Moin hier der Client'
bytesToSend = msgFromClient.encode( 'utf-8' )
UDPClient.sendto(bytesToSend, serverAddress )
# Warten auf Antwort
data,address =UDPClient.recvfrom(bufferSize)
#Daten vom Server erwarbeiten bzw. ausgeben..
data = data.decode( 'utf-8')
print( 'Data from Server: ', data)
print( 'Server IP Address: ', address[0])
print( 'Server Port: ', address[1])