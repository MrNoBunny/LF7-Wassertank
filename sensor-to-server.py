# Wichtige Bibliotheken
import socket # für UDP-Socket als Verbindung zum Server
import serial # für Serial-Verbindung zum Arduino
import time # für sleep Funktion
import threading # um zwei loops gleichzeitig laufen zu lassen

# Funktion zum Empfangen der Daten vom Arduino und weiterleiten an den Server
def arduino_pi_pi():
  #Socket/UDP-Verbindung zum Server erstellen
  serverAddress = ('192.168.123.10' , 2222)
  UDPClient = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
  while True:
    # Serial Connection auslesen
    if ser.in_waiting > 0:
      line = ser.readline().decode('utf-8').rstrip()

      # Daten auswerten
      # daten[0]: Wasserstand Tank 1 in cm
      # daten[1]: Wasserstand Tank 2 in cm
      # daten[2]: Abstand zum Wasser Tank 1 in cm
      # daten[3]: Abstand zum Wasser Tank 2 in cm
      daten = line.split(", ")

      # Wassermenge berechnen
      # wassermenge[0]: Wassermenge in Tank 1 in mL
      # wassermenge[1]: Wassermenge in Tank 2 in mL
      wassermenge = [str(round((3.1415*5.5*5.5*float(daten[0])))), str(round((3.1415*5.5*5.5*float(daten[1]))))]

      # Daten lokal anzeigen
      print("Tank 1: Wasserstand:",daten[0]+"cm | Wassermenge:",wassermenge[0]+"mL")
      print("Tank 2: Wasserstand:",daten[1]+"cm | Wassermenge:",wassermenge[1]+"mL")

      # Daten zum Server senden
      bytesToSend = daten[0]+", "+daten[1]+", "+wassermenge[0]+", "+wassermenge[1]
      bytesToSend = bytesToSend.encode('utf-8')
      UDPClient.sendto(bytesToSend, serverAddress)

      # Daten an Arduino senden
      if not (int(daten[0])<4) and not ((int(daten[3])<4) or (int(daten[3])>20)):
        print("Pumpen!")
        ser.write(b"PUMPEN\n ")
      #if (float(daten[1])<5) or (float(daten[1])>40):
      #  print("Tank 2 voll")
      #  ser.write(b"WARNING\n ")
    time.sleep(0.1)

# Funktion zum Empfangen von Befehlen vom Server und weiterleiten an den Arduino
def pi_pi_arduino():
  # Serveradreese definieren
  ServerPort = 2222
  ServerIP = '192.168.123.20'
  # Einen Socket starten, auf dem gelauscht werden soll
  RPIsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
  RPIsocket . bind ((ServerIP, ServerPort))
  print('Warte auf Befehle vom Server...')
  # Warten auf eine Anfrage..
  while True:
    befehl, address = RPIsocket.recvfrom(bufferSize)
    befehl = befehl.decode( 'utf-8' )
    print("Befehl erhalten von "+address[0]+":",befehl)
    # Befehl zum Pumpen an Arduino weiterleiten
    if befehl == "PUMPEN":
      ser.write(b"PUMPEN\n ")

if __name__ == '__main__':
  #Serielle Verbindung zum Arduino erstellen
  ser = serial.Serial( '/dev/ttyACM0' , 9600, timeout=1)
  ser.flush()

  # Buffer Size der UDP Sokets
  bufferSize = 1024

  # Die beiden Funktionen in zwei gleichzeitig laufenden Threads starten
  t1 = threading.Thread(target=arduino_pi_pi)
  t2 = threading.Thread(target=pi_pi_arduino)
  t1.start()
  t2.start()
  t1.join()
  t2.join()
  
  print('Ende')