//notes: set the led in pin 3,4,5 and the button to pin 2
int pin3val = 1;
int pin4val = 0;
int pin5val = 0;
void setup()
{
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(2, INPUT);
  Serial.begin(9600);
  digitalWrite(3, pin3val);
  digitalWrite(4, pin4val);
  digitalWrite(5, pin5val);
}

void loop()
{
  if (digitalRead(2) == HIGH)
  {
    Serial.print("Click");
    if(pin3val == 1)
    {
      pin3val = 0;
      pin4val = 1;
      pin5val = 0;
    }
    else if(pin4val == 1)
    {
      pin3val = 0;
      pin4val = 0;
      pin5val = 1;
    }
    else if(pin5val == 1)
    {
      pin3val = 1;
      pin4val = 0;
      pin5val = 0;
    }
  }
  digitalWrite(3, pin3val);
  digitalWrite(4, pin4val);
  digitalWrite(5, pin5val);
  delay(1000); // Wait for 1000 millisecond(s)
}