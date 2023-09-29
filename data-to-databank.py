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
  dateandtime = datetime.datetime.now()
  # Execute the sql script
  alldata = (wassertank1, wassertank2, dateandtime)
  sql = ("INSERT INTO tanks(tank1, tank2, timestamp)"
            "VALUES(%s,%s,%s)"
  )
  my_cursor.execute(sql, alldata)
  # confirm changes to the database
  my_db.commit()

  #Delete the last entry if the table has 60 entry
  #Select the count from the table
  my_cursor.execute("SELECT COUNT(*) FROM tanks")
  result = my_cursor.fetchone()

  if result[0] >= 60:
    my_cursor.execute("DELETE FROM tanks ORDER BY timestamp ASC LIMIT 1")
    my_db.commit