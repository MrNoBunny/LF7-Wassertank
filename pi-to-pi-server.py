# Einbinden der Bibliotheken
import socket
import time
bufferSize = 1024 # Wie viele Bytes sollen ausgetauscht werden?
ServerPort = 2222 # Freie Wahl eines verfügbaren Ports
ServerIP = '192.168.123.10' # Diese IP-Adresse muesst ihr vom Pi
# Versuch einen Socket zu starten, auf dem "Gelauscht" werden soll
RPIsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
RPIsocket . bind ((ServerIP, ServerPort))
print( 'Server läuft...')
# Warten auf eine Anfrage..
while True:
  message, address = RPIsocket.recvfrom(bufferSize)
  message = message.decode( 'utf-8' )
  print(message)
  print( 'Client Adresse = ',address[0])
  # Antworten mit den Sensordaten..
  #msgFromServer = "Hallo, hier ist der Server!" # hier sollten die
  #bytesToSend = msgFromServer.encode( 'utf-8') # Icodierte Nachricht
  #RPIsocket.sendto ( bytesToSend , address)