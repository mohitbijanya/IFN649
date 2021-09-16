#include "DHT.h"

#define SOILPIN 20      
#define PHOTOPIN 12
#define DHTPIN 21
#define DHTTYPE 11
DHT dht(DHTPIN,DHTTYPE);

#define rxPin 7 // Teensy pin 7 <--> HC-05 Tx
#define txPin 8 // Teensy pin 8 <--> HC-05 Rx

void setup() {
  // Setup serial for monitor
  Serial.begin(9600); 

  pinMode(SOILPIN, INPUT);
  pinMode(PHOTOPIN, INPUT);
  pinMode(DHTPIN, INPUT);
  dht.begin();

  // Setup Serial1 for BlueTooth
  Serial1.begin(9600); 
}

void loop() {
  
  displaySoil();
  displayPhotores();
  displayDHT();
  delay(1000);
}

void displaySoil()
{
  float val = analogRead(SOILPIN);
  
  Serial1.print(("SoilMoisture: "));
  Serial1.print(val);
  Serial.print(("SoilMoisture: "));
  Serial.print(val);
  
}

void displayPhotores()
{
  float val = analogRead(PHOTOPIN);
  Serial1.print(" Photoresistor: ");
  Serial1.print(val);
  Serial.print(" Photoresistor: ");
  Serial.print(val);
}

void displayDHT()
{
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  float hic = dht.computeHeatIndex(t, h, false);  

  Serial1.print((" Humidity: "));
  Serial1.print(h);
  Serial1.print((" Temperature: "));
  Serial1.println(t);


  Serial.print((" Humidity: "));
  Serial.print(h);
  Serial.print((" Temperature: "));
  Serial.println(t);


}

