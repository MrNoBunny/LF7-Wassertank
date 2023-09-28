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

import mysql.connector

my_db = mysql.connector.connect(
    host = "localhost",
    user = "tankadmin",
    password = "habehunger",
    database = "tanks",
)
my_cursor = my_db.cursor()

# Warten auf eine Anfrage..
while True:
  message, address = RPIsocket.recvfrom(bufferSize)
  message = message.decode( 'utf-8' )
  # Antworten mit den Sensordaten..
  daten = message.split(", ")
  #wasserdet = daten[0]

  #Daten des Wassertanks in Variablen teilen
  wassertank1 = daten[0]
  wassertank2 = daten[1]
  timestamp = datetime.datetime.now()
  # Execute the sql script
  my_cursor.execute("INSERT INTO tanks (tank1, tank2, timestamp)VALUES(%s;%s,%s)",
                    (wassertank1, wassertank2, timestamp)
  )
  # confirm changes to the database
  my_cursor.commit()
