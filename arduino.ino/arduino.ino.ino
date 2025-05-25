#include <Servo.h>

Servo myServo;
const int servoPin = A3;

void setup() {
  Serial.begin(9600);
  myServo.attach(servoPin);
  myServo.write(-90); // neutral position
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == 'f') {
      // Full forward and back
      myServo.write(90);
      delay(1000);
      myServo.write(0);
      delay(1000);
      myServo.write(-90); // Back to neutral
    }
  }
}
