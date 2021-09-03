#include "DHT.h"

String component_componentStatus;

#define DHTPIN 21
#define DHTTYPE 11
DHT dht(DHTPIN,DHTTYPE);


#define LEDPINRED 1

#define rxPin 7 // Teensy pin 7 <--> HC-05 Tx
#define txPin 8 // Teensy pin 8 <--> HC-05 Rx


void setup() {
  // Setup serial for monitor
  Serial.begin(9600); 

  pinMode(LEDPINRED, OUTPUT);
  pinMode(DHTPIN, INPUT);
  dht.begin();

  // Setup Serial1 for BlueTooth
  Serial1.begin(9600); 
}

void loop() {

  float t = dht.readTemperature();
  Serial1.println(t);
  
  if(Serial1.available() > 0)
  { // Checks whether data is comming from the serial port
    
    component_componentStatus = Serial1.readStringUntil('\n');
    component_componentStatus.trim();
    Serial.println(component_componentStatus);
    
    if(component_componentStatus == "RedLed_ON")
    {
        digitalWrite(LEDPINRED, HIGH);
    }
    else if(component_componentStatus == "RedLed_OFF")
    {
        digitalWrite(LEDPINRED, LOW);
    }
  }
   delay(1000);
}
