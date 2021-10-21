String component_componentStatus;

#define LEDPINRED 0
#define LEDPINYELLOW 1
#define LEDPINGREEN 2
#define BUZZERLPGPIN 3
#define BUZZERSMKPIN 4

#define rxPin 7 // Teensy pin 7 <--> HC-05 Tx
#define txPin 8 // Teensy pin 8 <--> HC-05 Rx


void setup() {
  // Setup serial for monitor
  Serial.begin(9600); 

  pinMode(LEDPINRED, OUTPUT);
  pinMode(LEDPINYELLOW, OUTPUT);
  pinMode(LEDPINGREEN, OUTPUT);
  pinMode(BUZZERLPGPIN, OUTPUT);
  pinMode(BUZZERSMKPIN, OUTPUT);

  // Setup Serial1 for BlueTooth
  Serial1.begin(9600);
}

void loop() {
  if(Serial1.available() > 0)
  { // Checks whether data is comming from the serial port
    
    component_componentStatus = Serial1.readStringUntil('\n');
    component_componentStatus.trim();
    Serial.println(component_componentStatus);

    //Leds
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

    //Buzzer

    if(component_componentStatus == "LPGBuzzer_ON")
    {
        digitalWrite(BUZZERLPGPIN, HIGH);
    }
    else if(component_componentStatus == "LPGBuzzer_OFF")
    {
        digitalWrite(BUZZERLPGPIN, LOW);
    }

    if(component_componentStatus == "SMKBuzzer_ON")
    {
        digitalWrite(BUZZERSMKPIN, HIGH);
    }
    else if(component_componentStatus == "SMKBuzzer_OFF")
    {
        digitalWrite(BUZZERSMKPIN, LOW);
    }

  }
}
