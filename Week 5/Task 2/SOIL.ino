#define SOILPIN 20      

#define LEDPIN 11
#define LEDPINGREEN 1
#define LEDPINYELLOW 2
#define LEDPINRED 3


#define rxPin 7 // Teensy pin 7 <--> HC-05 Tx
#define txPin 8 // Teensy pin 8 <--> HC-05 Rx

void setup() {
  // Setup serial for monitor
  Serial.begin(9600); 

  pinMode(SOILPIN, INPUT);

  pinMode(LEDPINRED, OUTPUT);
  pinMode(LEDPINYELLOW, OUTPUT);
  pinMode(LEDPINGREEN, OUTPUT);

  // Setup Serial1 for BlueTooth
  Serial1.begin(9600);
}

void loop() {
  digitalWrite(LEDPIN, HIGH);
    
  displaySoil();

  if(displaySoil() < 1)
  {
    digitalWrite(LEDPINRED, HIGH);
    digitalWrite(LEDPINYELLOW, LOW);
    digitalWrite(LEDPINGREEN, LOW);
  }
  else if(displaySoil() >= 1 && displaySoil() <= 50)
  {
    digitalWrite(LEDPINRED, LOW);
    digitalWrite(LEDPINYELLOW, HIGH);
    digitalWrite(LEDPINGREEN, LOW);
  }
  else if(displaySoil()>50)
  {
    digitalWrite(LEDPINRED, LOW);
    digitalWrite(LEDPINYELLOW, LOW);
    digitalWrite(LEDPINGREEN, HIGH);
  }
  
  delay(1000);
  digitalWrite(LEDPIN, LOW); 
  delay(1000);
}

int displaySoil()
{
  val = analogRead(SOILPIN);
  
  Serial1.print(("Soil Moisture = "));
  Serial1.print(val);

  return val;
}