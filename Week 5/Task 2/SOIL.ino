#define SOILPIN 20      
int val = 0;
int soilPower = 7;

#define LEDPIN 11
#define LEDPINGREEN 1
#define LEDPINYELLOW 2
#define LEDPINRED 3


#define rxPin 7 // Teensy pin 7 <--> HC-05 Tx
#define txPin 8 // Teensy pin 8 <--> HC-05 Rx

void setup() {
  // Setup serial for monitor
  Serial.begin(9600); 

  pinMode(soilPower, OUTPUT);//Set D7 as an OUTPUT
  digitalWrite(soilPower, LOW);//Set to LOW so no power is flowing through the sensor

  pinMode(LEDPINRED, OUTPUT);
  pinMode(LEDPINYELLOW, OUTPUT);
  pinMode(LEDPINGREEN, OUTPUT);

  // Setup Serial1 for BlueTooth
  Serial1.begin(9600); // Default communication rate of the Bluetooth module
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
  digitalWrite(soilPower, HIGH);//turn D7 "On"
  delay(10);//wait 10 milliseconds 
  val = analogRead(SOILPIN);//Read the SIG value form sensor 
  digitalWrite(soilPower, LOW);//turn D7 "Off"
  
  Serial1.println("Soil Moisture = ");
  //get soil moisture value from the function below and print it
  Serial1.println(val);

  return val;
}