import paho.mqtt.client as mqtt
import serial
import time
import string

ser = serial.Serial("/dev/rfcomm1", 9600)

def on_connect(client, userdata, flags, rc): # func for making connection
 print("Connected to MQTT")
 print("Connection returned result: " + str(rc) )
 client.subscribe("soilmoisture")
 client.subscribe("photoresistor")
 client.subscribe("humidity")
 client.subscribe("temperature")
 client.subscribe("heatindex")
 

def on_message(client, userdata, msg): # Func for Sending msg
 print(msg.topic+" "+str(msg.payload))
 
 if msg.topic == "soilmoisture":
     msgReceived = float(msg.payload.decode("utf-8"))
     print(msgReceived)
     if msgReceived > 50.0:
         ser.write(str.encode('RedLed_ON\r\n'))
     else:
         ser.write(str.encode('RedLed_OFF\r\n'))
     
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.loop_forever()