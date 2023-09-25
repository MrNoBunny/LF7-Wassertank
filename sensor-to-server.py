# Wichtige Bibliothek
import socket

import serial
import time

if __name__ == '__main__':
  #Serielle Verbindung zum Arduino erstellen
  ser = serial.Serial( '/dev/ttyACM0' , 9600, timeout=1)
  ser.flush()
  
  #Socket/UDP-Verbindung zum Server erstellen
  serverAddress = ('192.168.123.10' , 2222)
  bufferSize = 1024
  UDPClient = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
  
  while True:
    if ser.in_waiting > 0:
      line = ser.readline().decode('utf-8').rstrip()
      daten = line.split(", ")
      print("Temperatur:",daten[0]+"°C")
      print("Wasserstand:",daten[1])
      
      # Anfrage vom Client starten
      #msgFromClient ='Moin hier der Client'
      #bytesToSend = msgFromClient.encode( 'utf-8' )
      bytesToSend = line.encode( 'utf-8'  )
      UDPClient.sendto(bytesToSend, serverAddress )
      
      if(float(daten[0])>30):
        print("Zu heiß!")
        ser.write(b"HOT\n ")
      
# Warten auf Antwort
#data,address =UDPClient.recvfrom(bufferSize)
#Daten vom Server verarbeiten bzw. ausgeben..
#data = data.decode( 'utf-8')
#print( 'Data from Server: ', data)
#print( 'Server IP Address: ', address[0])
#print( 'Server Port: ', address[1])