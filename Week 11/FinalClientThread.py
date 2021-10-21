from threading import Thread 
import time
import paho.mqtt.client as mqtt
import serial
import time
import string

ser = serial.Serial("/dev/rfcomm3", 9600)

host_name = "54.91.133.214"

class ThdClass(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.mStop = False

	def run(self):
		while not self.mStop:
			print("Thread class")
			time.sleep(1)

		print('Thread class done!!')
			
	def stop(self):
		self.mStop = True

def on_connect(client, userdata, flags, rc): # func for making connection
 print("Connected to MQTT Server")
 print("Connection returned result: " + str(rc) )
 client.subscribe(userdata)
 
def on_message(client, userdata, msg): # Func for Sending msg
 msgRec = float(msg.payload.decode("utf-8"))
 print(msg.topic + "="+ str(msgRec))
 if msg.topic == "lpg":
     if msgRec > 0.020:
        ser.write(str.encode('LPGBuzzer_ON\r\n'))
     else:
        ser.write(str.encode('LPGBuzzer_OFF\r\n'))   
 if msg.topic == "smoke":
     if msgRec > 0.020:
        ser.write(str.encode('LPGBuzzer_ON\r\n'))
     else:
        ser.write(str.encode('LPGBuzzer_OFF\r\n'))
 if msg.topic == "temperature":
     if msgRec < 24.00:
         ser.write(str.encode('GreenLed_ON\r\n'))
         ser.write(str.encode('YellowLed_OFF\r\n'))
         ser.write(str.encode('RedLED_OFF\r\n'))
     elif msgRec > 24.00 and msgRec < 25.00 :
         ser.write(str.encode('YellowLed_ON\r\n'))
         ser.write(str.encode('GreenLed_OFF\r\n'))
         ser.write(str.encode('RedLed_OFF\r\n'))
     elif msgRec > 25.00:
         ser.write(str.encode('RedLed_ON\r\n'))
         ser.write(str.encode('GreenLed_OFF\r\n'))
         ser.write(str.encode('YellowLed_OFF\r\n'))
     

def Thdfunction(name,hostname, stop):
 client = mqtt.Client()
 client.on_connect = on_connect
 client.on_message = on_message
 client.user_data_set(name)
 client.connect(hostname, 1883, 60)
 client.loop_start()
 
 while not stop():
    print("Thread function " + name + " ")
    time.sleep(1)
    
 client.loop_stop()
 print('Thread function done!!')
 
def main():
 thdc = ThdClass()
 thdc.start()

 stop_thread = False
 thdf = Thread(target=Thdfunction, args=("lpg", host_name,lambda: stop_thread))
 thdf.start()
 
 thdf1 = Thread(target=Thdfunction, args=("co", host_name, lambda: stop_thread))
 thdf1.start()
 
 thdf2 = Thread(target=Thdfunction, args=("smoke", host_name,lambda: stop_thread))
 thdf2.start()

 thdf3 = Thread(target=Thdfunction, args=("humidity", host_name,lambda: stop_thread))
 thdf3.start()

 thdf4 = Thread(target=Thdfunction, args=("temperature", host_name,lambda: stop_thread))
 thdf4.start()

 thdf5 = Thread(target=Thdfunction, args=("heatindex", host_name,lambda: stop_thread))
 thdf5.start()

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
     thdf3.join()
     thdf4.join()
     thdf5.join()
     thdc.join()

if __name__ == "__main__":
    main()
