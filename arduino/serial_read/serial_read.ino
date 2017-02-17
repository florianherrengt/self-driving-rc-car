int x;
String str;

void setup()
{

  Serial.begin(250000);
  pinMode(8, OUTPUT); // left - brown
  pinMode(9, OUTPUT); // right - orange
  pinMode(10, OUTPUT); // backward - white
  pinMode(11, OUTPUT); // forward - blue
}

void loop()
{
    if(Serial.available() > 0)
    {
        str = Serial.readStringUntil('\n');
        if (str.equals("left_on")) {
          digitalWrite(9, LOW);
          digitalWrite(8, HIGH);
        }
        if (str.equals("right_on")) {
          digitalWrite(8, LOW);
          digitalWrite(9, HIGH);
        }
        if (str.equals("backward_on")) {
          digitalWrite(11, LOW);
          digitalWrite(10, HIGH);
        }
        if (str.equals("forward_on")) {
          digitalWrite(10, LOW);
          digitalWrite(11, HIGH);
        }
        if (str.equals("left_off")) {
          digitalWrite(8, LOW);
        }
        if (str.equals("right_off")) {
          digitalWrite(9, LOW);
        }
        if (str.equals("backward_off")) {
          digitalWrite(10, LOW);
        }
        if (str.equals("forward_off")) {
          digitalWrite(11, LOW);
        }
    }
}

