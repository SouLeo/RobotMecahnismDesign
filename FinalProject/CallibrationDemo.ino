#include "DualMC33926MotorShield.h"

// Encoder variables
#define outputA 6
#define outputB 7

int count = 0;
int currentState;
int prevState;

// Velocity variables 
int M1Speed;
int M2Speed;

// 
int controlMethod;
int totalCountsInRev = 64;
DualMC33926MotorShield md;

void setup()
{
  Serial.begin(115200);
  Serial.println("Dual MC33926 Motor Shield");
  // parameter declaration
  M1Speed = 0; // range [-400, 400]
  M2Speed = 0; // range [-400, 400]
  controlMethod = 0; // vel: 0, pos: 1
  if(controlMethod == 1){
    pinMode (outputA, INPUT);
    pinMode (outputB, INPUT);
    prevState = digitalRead(outputA);
  }
  
  md.init();
}

void loop()
{
  // velocity control
  if(controlMethod == 0){
    md.setM1Speed(M1Speed);
    stopIfFault();
    Serial.println("Motor 1 Speed: ");
    Serial.println(M1Speed, DEC);
    delay(2);
  }
  // pose control 
  // TODO: TEST IF THIS PRINTS PROPERLY AND CORRECT TOTALCOUNTSINREV
  if(controlMethod == 1){
    currentState = digitalRead(outputA);
    if (prevState != currentState){
      if (digitalRead(outputB) != currentState){
        count = (count + 1)%totalCountsInRev;  
      }
      else {
        count = count--;
        if (count < 0){
          count = 64;
        }
      }
    }
    currentState = prevState;
    Serial.println("Position: ");
    Serial.println(count);
  }
}

void stopIfFault()
{
  if (md.getFault())
  {
    Serial.println("fault");
    while(1);
  }
}
