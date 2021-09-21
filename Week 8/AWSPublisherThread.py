from threading import Thread 
import paho.mqtt.publish as publish
import time
import serial

ser = serial.Serial("/dev/rfcomm0", 9600)

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
        ser.close()

def Thdfunction(name,hostname, stop):
    while not stop():
        if ser.in_waiting > 0:
            rawserial = ser.readline()
            cookedserial = rawserial.decode('utf-8').strip('\r\n')
            message = cookedserial.strip().split()

            if name == "soilmoisture":
                publish.single(name, message[1], hostname=hostname)
            if name == "photoresistor":
                publish.single(name, message[3], hostname=hostname)
            if name == "humidity":
                publish.single(name, message[5], hostname=hostname)
            if name == "temperature":
                publish.single(name, message[7], hostname=hostname)

		print("Thread function" + name)
		time.sleep(1)

	print('Thread function done!!')

def main():
	thdc = ThdClass()
	thdc.start()

	stop_thread = False
    host_name = "54.234.134.21"
	thdf = Thread(target=Thdfunction, args=('soilmoisture', host_name, lambda: stop_thread))
	thdf.start()

    thdf1 = Thread(target=Thdfunction, args=('photoresistor', host_name, lambda: stop_thread))
	thdf1.start()

    thdf2 = Thread(target=Thdfunction, args=('humidity', host_name, lambda: stop_thread))
	thdf2.start()

    thdf3 = Thread(target=Thdfunction, args=('temperature', host_name, lambda: stop_thread))
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
        thdf3.join()
		thdc.join()

if __name__ == "__main__":
	main()