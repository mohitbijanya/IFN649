#include <MQ2.h>
//change this with the pin that you use
int pin = 13;

MQ2 mq2(pin);

void setup(){
  Serial.begin(9600);
  
  // calibrate the device
  mq2.begin();
}

void loop(){
  
  displayMQ2();
  delay(1000);
}

void displayMQ2()
{
   float* values= mq2.read(false); //set it false if you don't want to print the values to the Serial
   
   Serial.print("LPG: ");
   Serial.print(values[0], 3);
   Serial.print(" CO: ");
   Serial.print(values[1], 3);
   Serial.print(" Smoke: ");
   Serial.println(values[2], 3);
}