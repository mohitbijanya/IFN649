String component_componentStatus;

#define LEDPINRED 10
#define LEDPINYELLOW 9
#define LEDPINGREEN 6


#define rxPin 7 // Teensy pin 7 <--> HC-05 Tx
#define txPin 8 // Teensy pin 8 <--> HC-05 Rx


void setup() {
  // Setup serial for monitor
  Serial.begin(9600); 

  pinMode(LEDPINRED, OUTPUT);
  pinMode(LEDPINYELLOW, OUTPUT);
  pinMode(LEDPINGREEN, OUTPUT);

  // Setup Serial1 for BlueTooth
  Serial1.begin(9600); 
}

void loop() {
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
    if(component_componentStatus == "YellowLed_ON")
    {
        digitalWrite(LEDPINYELLOW, HIGH);
    }
    else if(component_componentStatus == "YellowLed_OFF")
    {
        digitalWrite(LEDPINYELLOW, LOW);
    }
    if(component_componentStatus == "GreenLed_ON")
    {
        digitalWrite(LEDPINGREEN, HIGH);
    }
    else if(component_componentStatus == "GreenLed_OFF")
    {
        digitalWrite(LEDPINGREEN, LOW);
    }
  }
   delay(1000);
}
