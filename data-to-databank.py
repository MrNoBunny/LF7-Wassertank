# Einbinden der Bibliotheken
import socket
import time
import datetime
bufferSize = 1024 # Wie viele Bytes sollen ausgetauscht werden?
ServerPort = 2222 # Freie Wahl eines verfuegbaren Ports
ServerIP = '192.168.123.10' # Diese IP-Adresse muesst ihr vom Pi
# Versuch einen Socket zu starten, auf dem "Gelauscht" werden soll
RPIsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
RPIsocket . bind ((ServerIP, ServerPort))
print( 'Server laeuft...')

# Einbinden des Datenbanksmodul
import mysql.connector

# Verbinden mit der Datenbank
my_db = mysql.connector.connect(
    host = "localhost",
    user = "tankadmin",
    password = "habehunger",
    database = "tanks",
)

# Einen Cursor vordefinieren, um die Eingabeaufforderungen in der Datenbank auszuführen
my_cursor = my_db.cursor()

# Warten auf eine Anfrage..
while True:
  message, address = RPIsocket.recvfrom(bufferSize)
  message = message.decode( 'utf-8' )
  # Antworten mit den Sensordaten..
  daten = message.split(", ")
  #wasserdet = daten[0]

  #Daten des Wassertanks in Variablen einteilen
  wassertank1 = daten[0]
  wassertank2 = daten[1]
  wassermenge1 = daten[2]
  wassermenge2 = daten[3]
  dateandtime = datetime.datetime.now()
  # Alle Daten in eine Tabelle hinzugefügen
  alldata = (wassertank1, wassermenge1, wassertank2, wassermenge2, dateandtime)
  # SQL Skript Variable vordefinieren ( %s Patzhalten für die Daten in $alldata)
  sql = ("INSERT INTO tanks(tank1, wassermenge1, tank2, wassermenge2, timestamp)"
            "VALUES(%s,%s,%s,%s,%s)"
  )
  # Das SQL Skript ausführen
  my_cursor.execute(sql, alldata)
  # Die Änderung in der Datenbank genehmigen
  my_db.commit()

  # Den letzten Speicher der Datenbank löschen, wenn die Anzahl bei 60 liegt
  my_cursor.execute("SELECT COUNT(*) FROM tanks")
  result = my_cursor.fetchone()

  if result[0] >= 60:
    my_cursor.execute("DELETE FROM tanks ORDER BY timestamp ASC LIMIT 1")
    my_db.commit