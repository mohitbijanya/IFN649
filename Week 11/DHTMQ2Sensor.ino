#include "DHT.h"
#include <MQ2.h>

#define MQ2PIN 13
#define DHTPIN 21
#define DHTTYPE 11

DHT dht(DHTPIN,DHTTYPE);
MQ2 mq2(MQ2PIN);

#define rxPin 7 // Teensy pin 7 <--> HC-05 Tx
#define txPin 8 // Teensy pin 8 <--> HC-05 Rx

void setup() {
  // Setup serial for monitor
  Serial.begin(9600); 

  pinMode(MQ2PIN, INPUT);
  pinMode(DHTPIN, INPUT);
  dht.begin();
  mq2.begin();

  // Setup Serial1 for BlueTooth
  Serial1.begin(9600); 
}

void loop() {
  
  displayMQ2();
  Serial.print(" ");
  displayDHT();
  Serial.println();
  delay(30000);
}

void displayDHT()
{
  float h = dht.readHumidity();
  float t = dht.readTemperature(); 

  Serial1.print(("Humidity: "));
  Serial1.print(h);
  Serial1.print((" Temperature: "));
  Serial1.print(t);

  Serial.print(("Humidity: "));
  Serial.print(h);
  Serial.print((" Temperature: "));
  Serial.print(t);
}

void displayMQ2()
{
   float* values= mq2.read(false); //set it false if you don't want to print the values to the Serial

   Serial1.print("LPG: ");
   Serial1.print(values[0], 3);
   Serial1.print(" CO: ");
   Serial1.print(values[1], 3);
   Serial1.print(" Smoke: ");
   Serial1.print(values[2], 3);

   Serial.print("LPG: ");
   Serial.print(values[0], 3);
   Serial.print(" CO: ");
   Serial.print(values[1], 3);
   Serial.print(" Smoke: ");
   Serial.print(values[2], 3);
}

