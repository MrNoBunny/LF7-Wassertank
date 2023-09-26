# Einbinden der Bibliotheken
import socket
import time
bufferSize = 1024 # Wie viele Bytes sollen ausgetauscht werden?
ServerPort = 2222 # Freie Wahl eines verfuegbaren Ports
ServerIP = '192.168.123.10' # Diese IP-Adresse muesst ihr vom Pi
# Versuch einen Socket zu starten, auf dem "Gelauscht" werden soll
RPIsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
RPIsocket . bind ((ServerIP, ServerPort))
print( 'Server laeuft...')
# Warten auf eine Anfrage..
while True:
  message, address = RPIsocket.recvfrom(bufferSize)
  message = message.decode( 'utf-8' )
  # Antworten mit den Sensordaten..
  daten = message.split(", ")
  wasserdet = daten[0]
  wassersta = daten[1]
  print("Wasserdetektor:",wasserdet)
  print("Wasserstand:",wassersta ,"cm")