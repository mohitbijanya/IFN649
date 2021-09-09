#include "DHT.h"

#define SOILPIN 20      
#define PHOTOPIN 12

#define DHTPIN 21
#define DHTTYPE 11
DHT dht(DHTPIN,DHTTYPE);

#define LEDPINGREEN 1
#define LEDPINYELLOW 2
#define LEDPINRED 3
#define BUZZERPIN 4

#define rxPin 7 // Teensy pin 7 <--> HC-05 Tx
#define txPin 8 // Teensy pin 8 <--> HC-05 Rx

String component_componentStatus;

void setup() {
  // Setup serial for monitor
  Serial.begin(9600); 

  pinMode(SOILPIN, INPUT);
  pinMode(PHOTOPIN, INPUT);
  pinMode(DHTPIN, INPUT);
  dht.begin();

  pinMode(LEDPINRED, OUTPUT);
  pinMode(LEDPINYELLOW, OUTPUT);
  pinMode(LEDPINGREEN, OUTPUT);
  pinMode(BUZZERPIN,OUTPUT);

  // Setup Serial1 for BlueTooth
  Serial1.begin(9600);
}

void loop() {

  displaySoil();
  displayPhotores();
  displayDHT();
  
  if(Serial1.available() > 0)
  { // Checks whether data is comming from the serial port
    
    component_componentStatus = Serial1.readString();
    component_componentStatus.trim();
    
    Serial1.println(component_componentStatus);
    
    if(component_componentStatus == "RedLed_ON")
    {
        digitalWrite(LEDPINRED, HIGH);
    }
    else if(component_componentStatus == "RedLed_OFF")
    {
        digitalWrite(LEDPINRED, LOW);
    }
    else if(component_componentStatus == "Buzzer_ON")
    {
      digitalWrite(BUZZERPIN, HIGH);
    }
    else if(component_componentStatus == "Buzzer_OFF")
    {
      digitalWrite(BUZZERPIN, LOW);
    }

   
  }
   delay(1000);
}

int displaySoil()
{
  val = analogRead(SOILPIN);
  
  Serial1.print(("Soil Moisture = "));
  Serial1.print(val);

  return val;
}

int displayPhotores()
{
  val = analogRead(PHOTOPIN);
  Serial1.print("Photoresistor value = ");
  Serial1.print(val);
}

void displayDHT()
{
    float h = dht.readHumidity();
    float t = dht.readTemperature();
    float f = dht.readTemperature(true);

    float hif = dht.computeHeatIndex(f, h);
    float hic = dht.computeHeatIndex(t, h, false);  

    Serial1.print(F(" Humidity: "));
    Serial1.print(h);
    Serial1.print(F("%  Temperature: "));
    Serial1.print(t);
    Serial1.print(F("C "));
    Serial1.print(f);
    Serial1.print(F("F  Heat index: "));
    Serial1.print(hic);
    Serial1.print(F("C "));
    Serial1.print(hif);
    Serial1.println(F("F"));
}

