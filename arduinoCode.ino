#include<Servo.h>
const int buzzer = 11; 
Servo myservo;
char d;
int pos;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(5,OUTPUT);
myservo.attach(9); 
  myservo.write(0);
}

void loop() {
  // put your main code here, to run repeatedly:
if(Serial.available())
{
  d=Serial.read();
}
if(d=='a')
{
  Serial.print(d);
  delay(300);
  for(pos=0;pos<=90;pos+=5)
   { myservo.write(pos);
   delay(20);
   }
   delay(5000);
   for(pos=90;pos>=0;pos-=5)
   { 
   myservo.write(pos);
   delay(20);
   }
   d=' ';
   }
   

if(d=='u'){
  Serial.print(d);
  delay(300);
  int i=0;
  do{
    i++;
    tone(buzzer,500);
    delay(200);
    noTone(buzzer);
    delay(200);
  }while(i<5);
  delay(100);
  digitalWrite(buzzer,LOW);
  d=' ';
  }
}
