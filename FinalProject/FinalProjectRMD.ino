#include "DualMC33926MotorShield.h"

DualMC33926MotorShield md;

int motor_speed = 225;
int motor_direction = 0;

int control_switch = 6;
int control_switch_current_status = LOW;
int control_switch_past_status = LOW;

void stopIfFault()
{
  if (md.getFault())
  {
    Serial.println("fault");
    while(1);
  }
}

void setup()
{
  Serial.begin(115200);
  Serial.println("Dual MC33926 Motor Shield");
  pinMode(control_switch, INPUT);  
  md.init();
}

void loop()
{
  if (Serial.available() > 0){
    if (Serial.read()){
        Serial.println("hi");
        md.setM1Speed(-10);
        delay(100000);
      }
  }
  md.setM1Speed(motor_speed);
}
