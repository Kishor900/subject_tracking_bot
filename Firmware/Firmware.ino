
// Include Libraries
#include "Arduino.h"
#include "DCMDriverL298.h"

#define BLYNK_PRINT Serial
#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>

// You should get Auth Token in the Blynk App.
// Go to the Project Settings (nut icon).
char auth[] = "";

// Your WiFi credentials.
// Set password to "" for open networks.
char ssid[] = "";
char pass[] = "";
// Pin Definitions
#define DCMOTORDRIVERL298_PIN_INT1  5
#define DCMOTORDRIVERL298_PIN_ENB 14
#define DCMOTORDRIVERL298_PIN_INT2  0
#define DCMOTORDRIVERL298_PIN_ENA 4
#define DCMOTORDRIVERL298_PIN_INT3  2
#define DCMOTORDRIVERL298_PIN_INT4  12

DCMDriverL298 dcMotorDriverL298(DCMOTORDRIVERL298_PIN_ENA, DCMOTORDRIVERL298_PIN_INT1, DCMOTORDRIVERL298_PIN_INT2, DCMOTORDRIVERL298_PIN_ENB, DCMOTORDRIVERL298_PIN_INT3, DCMOTORDRIVERL298_PIN_INT4);
// Setup the essentials for your circuit to work. It runs first every time your circuit is powered with electricity.
void setup()
{
  Serial.begin(9600);
  Blynk.begin(auth, ssid, pass);
  while (!Serial) ; // wait for serial port to connect. Needed for native USB
  Serial.println("start");
  pinMode(D7, INPUT);
  pinMode(D8, INPUT);
  pinMode(D9, INPUT);
}

// Main logic of your circuit. It defines the interaction between the components you selected. After setup, it runs over and over again, in an eternal loop.
void loop()
{
  if (digitalRead(D7) == 1) {
    forward();
    Serial.println("moving forward");
  } else {
    stopMotors();
  }
  if (digitalRead(D8) == 1) {
    left();
    Serial.println("moving left");
  } else {
    stopMotors();
  }
  if (digitalRead(D9) == 1) {
    right();
    Serial.println("moving right");
  } else {
    stopMotors();
  }
  Blynk.run();
}
void forward() {
  dcMotorDriverL298.setMotorA(255, 1);
  dcMotorDriverL298.setMotorB(255, 0);
}
void left() {
  dcMotorDriverL298.setMotorA(255, 1);
  dcMotorDriverL298.setMotorB(255, 1);
}
void right() {
  dcMotorDriverL298.setMotorA(255, 0);
  dcMotorDriverL298.setMotorB(255, 0);
}
void stopMotors() {
  dcMotorDriverL298.stopMotors();
}
