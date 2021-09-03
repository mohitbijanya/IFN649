import serial
import time
import string
# reading and writing data from and to arduino serially.
# rfcomm0 -> this could be different
ser = serial.Serial("/dev/rfcomm0", 9600)
while True:
 if ser.in_waiting > 0:
     rawserial = ser.readline()
     cookedserial = rawserial.decode('utf-8').strip('\r\n')
     print(cookedserial)
     intserial = float(cookedserial)
     
     #this parameters are oonly done like this
     #because the dht value tend to not go down
     if intserial > 25.00:
         ser.write(str.encode('RedLed_OFF\r\n'))
     elif intserial > 24.95:
         ser.write(str.encode('RedLed_ON\r\n'))
     else:
         ser.write(str.encode('RedLed_OFF\r\n'))
