#include <Servo.h>
float X,Y,Z;
int angel_Arm_one,angel_Arm_two,angel_top;
char cmd_1,cmd_2;

Servo servo_bottom;
Servo servo_Arm_one;
Servo servo_Arm_two;
Servo servo_top;


void setup() {
  Serial.begin(9600);
  servo_bottom.attach(6);
  servo_Arm_one.attach(9);
  servo_Arm_two.attach(10);
  servo_top.attach(11);
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
}
void loop(){
  if(Serial.available()){
    cmd_1 = Serial.read();
    while(!Serial.read()){
    }
    cmd_2 = Serial.read();
  }

}
void solve(){
  float x,y;
  x = X/30;
  y = y/30;
  float a;
  a = atan(sqrt(4/(x*x+y*y)-1));
  angel_Arm_one = int(a + atan(X/Y));
  angel_Arm_two = int(180 - 2*a);
}
