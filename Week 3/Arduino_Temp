//notes: set the 3 LED to pin 2,3,4 and the temp sensor to pin A0

float temp;

void setup()
{
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(A0, INPUT);
  Serial.begin(9600);
}

void loop()
{
  float currentTemperature = temp_read(temp, A0);
  led_write(currentTemperature);
  delay(1000);
}

float temp_read(float t, int p)
{
	t = analogRead(p);
    t = t * 5;
    t = t /1024;
  	t = (t-0.5) * 100;
  	Serial.print("TEMPERATURE = ");
  	Serial.print(t); 
  	Serial.print(" C");
  	Serial.println();
  	return t;
}

void led_write(float t)
{
  if(t < 12.5)
  {
    digitalWrite(2,HIGH);
    digitalWrite(3,LOW);
    digitalWrite(4,LOW);
  }
  else if(t >= 12.5 && t <= 30)
  {
    digitalWrite(2,LOW);
    digitalWrite(3,HIGH);
    digitalWrite(4,LOW);
    
  }
  else if(t > 30)
  {
    digitalWrite(2,LOW);
    digitalWrite(3,LOW);
    digitalWrite(4,HIGH);
  }
}

