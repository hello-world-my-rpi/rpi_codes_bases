# rpi_codes_bases
Only for my raspberry pi clock to update.
If anbody else find these codes,you can also use them free.
But,they are not pretty,even bad in some ways.
2019/9/15


float X,Y,Z;
boolean situ = false;
char mesg;
char old_mesg;
int angel_one,angel_two;
void slove(float x,float y){
  float angel_o,angel_t,a;
  
  x = x/10;
  y = y/10;
  /*---------------------------*/
  a = atan(sqrt((4/(x*x + y*y))-1));
  angel_o = a + atan(y/x);
  angel_t = 180 - 2*a;
  /*---------------------------*/
  angel_one = angel_o;
  angel_two = angel_t;
}
void setup() {
  Serial.begin(9600);
}

void loop() {
  if(Serial.available()){
    mesg = Serial.read();
  }
  if(mesg != old_mesg){
    if(mesg == "a"){
      X += 1;
    }
    else if(mesg == "b"){
      X += -1;
    }
    else if(mesg == "c"){
      Y += 1;
    }
    else if(mesg == "d"){
      Y -= 1;
    }
    old_mesg = mesg;  
    slove(X,Y);
    Serial.println(angel_one,angel_two);
  } 
}
