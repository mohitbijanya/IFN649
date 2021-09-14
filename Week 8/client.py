import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc): # func for making connection
 print("Connected to MQTT")
 print("Connection returned result: " + str(rc) )
 client.subscribe("soilmoisture")
 

def on_message(client, userdata, msg): # Func for Sending msg
 print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
print(on_message.msg.topic + "success")
client.connect("172.31.20.137", 1883, 60)
client.loop_forever()