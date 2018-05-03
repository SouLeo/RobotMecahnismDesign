#include "DualMC33926MotorShield.h"

DualMC33926MotorShield md;

int motor_speed = 200;
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
  /*
   * TODO TEST:
   * 1. Set angle limits on motor
   * 2. Make a button start and stop the system
   * 3. Make a change direction button
   * 4. PID control on motor speed
   */
   
 /*
  if (Serial.available() > 0){
    if (Serial.read()){
        Serial.println("hi");
        md.setM1Speed(-10);
        delay(100000);
      }
  }
  md.setM1Speed(motor_speed);
*/

 
  control_switch_current_status = digitalRead(control_switch);
  if (control_switch_current_status == HIGH) {
    Serial.println("Switch Hit");
    Serial.println("Stopping!");
    md.setM1Speed(0);
    delay(100);
    Serial.println("UP");
    md.setM1Speed(motor_speed);
    delay(3000);
    Serial.println("Stopping!");
    delay(1000);
    Serial.println("DOWN");
    md.setM1Speed(-10);
    delay(3000);    
  }


}
