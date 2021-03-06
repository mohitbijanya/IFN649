from threading import Thread 
import time
import paho.mqtt.client as mqtt
import serial
import time
import string

ser = serial.Serial("/dev/rfcomm3", 9600)

class ThdClass(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.mStop = False

	def run(self):
		while not self.mStop:
			#print("Thread class")
			time.sleep(1)

		print('Thread class done!!')
			
	def stop(self):
		self.mStop = True

def on_connect(client, userdata, flags, rc): # func for making connection
 print("Connected to MQTT Server")
 print("Connection returned result: " + str(rc) )
 client.subscribe(userdata)
 
def on_message(client, userdata, msg): # Func for Sending msg
 time.sleep(1)
 msgRec = float(msg.payload.decode("utf-8"))
 print(msg.topic + "="+ str(msgRec))
 if msg.topic == "soilmoisture":
     if msgRec > 50.00:
        ser.write(str.encode('\nRedLed_ON\n'))
     else:
        ser.write(str.encode('\nRedLed_OFF\n'))
 if msg.topic == "photoresistor":
     if msgRec > 50.00:
        ser.write(str.encode('\nYellowLed_ON\n'))
     else:
        ser.write(str.encode('\nYellowLed_OFF\n'))
 if msg.topic == "temperature":
     if msgRec > 25.00:
        ser.write(str.encode('\nGreenLed_ON\n'))
     else:
        ser.write(str.encode('\nGreenLed_OFF\n')) 

def Thdfunction(name, stop):
 client = mqtt.Client()
 client.on_connect = on_connect
 client.on_message = on_message
 client.user_data_set(name)
 client.connect("localhost", 1883, 60)
 client.loop_start()
 
 while not stop():
    #print("Thread function " + name + " ")
    time.sleep(1)
    
 client.loop_stop()
 print('Thread function done!!')
 
def main():
 thdc = ThdClass()
 thdc.start()

 stop_thread = False
 thdf = Thread(target=Thdfunction, args=("soilmoisture", lambda: stop_thread))
 thdf.start()
 
 thdf1 = Thread(target=Thdfunction, args=("photoresistor", lambda: stop_thread))
 thdf1.start()
 
 thdf2 = Thread(target=Thdfunction, args=("temperature", lambda: stop_thread))
 thdf2.start()
 
 thdf3 = Thread(target=Thdfunction, args=("humidity", lambda: stop_thread))
 thdf3.start()

 try:
  while True:
   cmd = input()
   if(cmd =='q'):
     print('stopping.....')
     thdc.stop()
     stop_thread = True
     break;
   print('Main Thread')

 except KeyboardInterrupt:
     thdc.stop()
     stop_thread = True
 finally:
     thdf.join()
     thdf1.join()
     thdf2.join()
     thdc.join()

if __name__ == "__main__":
    main()
