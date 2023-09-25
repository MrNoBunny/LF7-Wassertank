import serial
import time

if __name__ == '__main__':
  ser = serial.Serial( '/dev/ttyACM0' , 9600, timeout=1)
  ser.flush()

  while True:
    if ser.in_waiting > 0:
      line = ser.readline().decode('utf-8').rstrip()
      print(line)
      if(float(line)>30):
        print("Zu heiß!")
        ser.write(b"HOT\n")

#testen ob es pushed