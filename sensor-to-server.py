# Wichtige Bibliotheken
import socket # fuer UDP-Socket als Verbindung zum Server
import serial # fuer Serial-Verbindung zum Arduino
import time # fuer sleep Funktion
import threading # um zwei loops gleichzeitig laufen zu lassen

pumpe1 = False
pumpe2 = False

# Funktion zum Empfangen der Daten vom Arduino und weiterleiten an den Server
def arduino_pi_pi():
  global pumpe1
  global pumpe2
  #Socket/UDP-Verbindung zum Server erstellen
  serverAddress = ('192.168.123.10' , 2222)
  UDPClient = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
  while True:
    # Serial Connection auslesen
    if ser.in_waiting > 0:
      line = ser.readline().decode('utf-8').rstrip()
      daten = line.split(", ")
      wassermenge = [str(round((3.1415*5.5*5.5*float(daten[0])))), str(round((3.1415*5.5*5.5*float(daten[1]))))]

      # Daten lokal anzeigen
      print("Tank 1: Wasserstand:",daten[0]+"cm | Wassermenge:",wassermenge[0]+"mL")
      print("Tank 2: Wasserstand:",daten[1]+"cm | Wassermenge:",wassermenge[1]+"mL")

      # Daten zum Server senden
      bytesToSend = daten[0]+", "+daten[1]+", "+wassermenge[0]+", "+wassermenge[1]
      bytesToSend = bytesToSend.encode('utf-8')
      UDPClient.sendto(bytesToSend, serverAddress)

      # Daten an Arduino senden
      if not (int(daten[0])<5) and not ((int(daten[3])<4) or (int(daten[3])>20)) and not pumpe2 and not pumpe1:
        print("Pumpen!")
        ser.write(b"PUMPEN_1")
        pumpe1 = True
      if (int(daten[0])<4) and not pumpe2 and pumpe1:
        print("Pumpe 1 stopp!")
        ser.write(b"\nSTOPP\n ")
        pumpe1 = False
    time.sleep(0.1)

# Funktion zum Empfangen von Befehlen vom Server und weiterleiten an den Arduino
def pi_pi_arduino():
  global pumpe2
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
      ser.write(b"PUMPEN_2")
      pumpe2 = True
    if befehl == "STOPP":
      ser.write(b"\nSTOPP\n ")
      pumpe2 = False

if __name__ == '__main__':
  #Serielle Verbindung zum Arduino erstellen
  try:
    ser = serial.Serial( '/dev/ttyACM0' , 9600, timeout=1)
  except:
    ser = serial.Serial( '/dev/ttyACM1' , 9600, timeout=1)
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
