import paho.mqtt.publish as publish
import serial
import time
import string
import blynklib

ser = serial.Serial("/dev/rfcomm0", 9600)
blynk = blynklib.Blynk('G3zAPk6quYmDFXvp4ZKzMd6-txV38zKz')

while True:
 blynk.run()
 if ser.in_waiting > 0:
     rawserial = ser.readline()
     cookedserial = rawserial.decode('utf-8').strip('\r\n')

     message = cookedserial.strip().split()
     
     publish.single("lpg", message[1], hostname="localhost")
     publish.single("co", message[3], hostname="localhost")
     publish.single("smoke", message[5], hostname="localhost")
     publish.single("humidity", message[7], hostname="localhost")
     publish.single("temperature", message[9], hostname="localhost")
     publish.single("heatindex", message[11], hostname="localhost")

     blynk.virtual_write(0, message[1])
     blynk.virtual_write(1, message[3])
     blynk.virtual_write(2, message[5])
     blynk.virtual_write(3, message[7])
     blynk.virtual_write(4, message[9])
     blynk.virtual_write(5, message[11])
     print(message)