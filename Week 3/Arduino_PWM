//notes: set the led in pin 3 and the button to pin 2

int val = 0;
void setup()
{
  pinMode(2, INPUT);
  pinMode(3, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  if (digitalRead(2) == HIGH) 
  {
    val = val + 51;
    if(val > 255)
    {
      val = 0;
    }
    
    Serial.print("Click, val = ");
  	Serial.print(val);
  	Serial.println();
  }
  
  analogWrite(3, val);
  delay(1000);
}