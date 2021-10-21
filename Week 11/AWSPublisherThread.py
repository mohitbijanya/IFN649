from threading import Thread 
import paho.mqtt.publish as publish
import time
import serial
import blynklib

ser = serial.Serial("/dev/rfcomm0", 9600)
blynk = blynklib.Blynk('G3zAPk6quYmDFXvp4ZKzMd6-txV38zKz')
host_name = "54.234.134.21"

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
		#close serial here
        ser.close()

def Thdfunction(name,hostname, stop):
    while not stop():
        if ser.in_waiting > 0:
            rawserial = ser.readline()
            cookedserial = rawserial.decode('utf-8').strip('\r\n')
            message = cookedserial.strip().split()

            if name == "lpg":
                publish.single(name, message[1], hostname=hostname)
				blynk.virtual_write(0, message[1])
            if name == "co":
                publish.single(name, message[3], hostname=hostname)
				blynk.virtual_write(1, message[3])
			if name == "smoke":
				publish.single(name, message[5], hostname=hostname)
				blynk.virtual_write(2, message[5])
            if name == "humidity":
                publish.single(name, message[7], hostname=hostname)
				blynk.virtual_write(3, message[7])
            if name == "temperature":
                publish.single(name, message[9], hostname=hostname)
				blynk.virtual_write(4, message[9])
			if name == "heatindex":
				publish.single(name, message[11], hostname=hostname)
				blynk.virtual_write(5, message[11])

		print("Thread function" + name)
		print(message)
		time.sleep(1)

	print('Thread function done!!')

def main():
	thdc = ThdClass()
	thdc.start()

	stop_thread = False
	thdf = Thread(target=Thdfunction, args=('lpg', host_name, lambda: stop_thread))
	thdf.start()

    thdf1 = Thread(target=Thdfunction, args=('co', host_name, lambda: stop_thread))
	thdf1.start()

    thdf2 = Thread(target=Thdfunction, args=('smoke', host_name, lambda: stop_thread))
	thdf2.start()

    thdf3 = Thread(target=Thdfunction, args=('humidity', host_name, lambda: stop_thread))
	thdf3.start()

	thdf4 = Thread(target=Thdfunction, args=("temperature", host_name,lambda: stop_thread))
    thdf4.start()

	thdf5 = Thread(target=Thdfunction, args=("heatindex", host_name,lambda: stop_thread))
    thdf5.start()
	
	try:
		while True:
			blynk.run()
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