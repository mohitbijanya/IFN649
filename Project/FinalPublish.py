import paho.mqtt.publish as publish
import serial
import time
import string
import blynklib

ser = serial.Serial("/dev/rfcomm0", 9600)
blynk = blynklib.Blynk('G3zAPk6quYmDFXvp4ZKzMd6-txV38zKz')
host_name = "34.229.92.150"

try:
    while True:
     blynk.run()
     if ser.in_waiting > 0:
         rawserial = ser.readline()
         cookedserial = rawserial.decode('utf-8').strip('\r\n')

         message = cookedserial.strip().split()
         
         publish.single("lpg", message[1], hostname=host_name)
         publish.single("co", message[3], hostname=host_name)
         publish.single("smoke", message[5], hostname=host_name)
         publish.single("humidity", message[7], hostname=host_name)
         publish.single("temperature", message[9], hostname=host_name)
         publish.single("HeatIndex", message[11], hostname=host_name)

         blynk.virtual_write(0, message[1])
         blynk.virtual_write(1, message[3])
         blynk.virtual_write(2, message[5])
         blynk.virtual_write(3, message[7])
         blynk.virtual_write(4, message[9])
         blynk.virtual_write(5, message[11])
         
         if float(message[5]) > 20.000 and float(message[9]) > 30.00:
             blynk.notify("Critical Alert...Fire Detected...!!!")
         if float(message[1]) > 5.000:
             blynk.notify("Alert...Gas Leak...!!!")
         elif float(message[5]) > 20.000: 
             blynk.notify("Alert...Smoke Detected...!!!")
         

   
         print(message)
         
except KeyboardInterrupt:
    ser.close()
    print("Serial closed")