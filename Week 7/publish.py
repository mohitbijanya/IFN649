import paho.mqtt.publish as publish
import serial
import time
import string

ser = serial.Serial("/dev/rfcomm0", 9600) # can change

while True:
 if ser.in_waiting > 0:
    rawserial = ser.readline()
    cookedserial = rawserial.decode('utf-8').strip('\r\n')

    message = cookedserial.strip().split()

    publish.single("soilmoisture", message[1], hostname="localhost")
    publish.single("photoresistor", message[3], hostname="localhost")
    publish.single("humidity", message[5], hostname="localhost")
    publish.single("temperature", message[7], hostname="localhost")
    publish.single("heatindex", message[9], hostname="localhost")
     
    print("Done")
