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
    # Serial Connection auslesen
    if ser.in_waiting > 0:
      line = ser.readline().decode('utf-8').rstrip()

      # Daten auswerten
      daten = line.split(", ")

      #if (float(daten[0]) > 100):
      #  regen = True
      #else:
      #  regen = False

      # Daten lokal anzeigen
      #print("Regnen:", regen)
      print("Wasserstand Tank 1:",daten[0]+"cm Luft im Tank")
      print("Wasserstand Tank 2:",daten[1]+"cm Luft im Tank")

      # Daten zum Server senden
      bytesToSend = daten[0]+", "+daten[1]
      bytesToSend = bytesToSend.encode('utf-8')
      UDPClient.sendto(bytesToSend, serverAddress)

      # Daten an Arduino senden
      if (float(daten[0])<5) or (float(daten[0])>40):
        print("Tank 1 voll")
        ser.write(b"WARNING\n ")
      if (float(daten[1])<5) or (float(daten[1])>40):
        print("Tank 2 voll")
        ser.write(b"WARNING\n ")

    time.sleep(0.1)

# Warten auf Antwort
#data,address =UDPClient.recvfrom(bufferSize)
#Daten vom Server verarbeiten bzw. ausgeben..
#data = data.decode( 'utf-8')
#print( 'Data from Server: ', data)
#print( 'Server IP Address: ', address[0])
#print( 'Server Port: ', address[1])