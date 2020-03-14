// #include <Arduino.h>
// #include <stdio.h>

// const int moistureSensor0 = A3;
// const int moistureSensor1 = A4;
// const int moistureSensor2 = A5;
// const int moistureSensor3 = A6;
// const int moistureSensor4 = A7;
// const int power0 = 3;
// const int power1 = 2;


// void setup() {
//   Serial.begin(9600);
//   pinMode(power0, OUTPUT);
//   pinMode(power1, OUTPUT); 
// }

// void loop() {
//   digitalWrite(power0, HIGH);
//   digitalWrite(power1, HIGH);
//   delay(1000);
//   int sensorValue0 = analogRead(moistureSensor0);
//   int sensorValue1 = analogRead(moistureSensor1);
//   int sensorValue2 = analogRead(moistureSensor2);
//   int sensorValue3 = analogRead(moistureSensor3);
//   int sensorValue4 = analogRead(moistureSensor4);
//   delay(1000);
//   float percentage0 = (1024.0f-sensorValue0)/10.24;
//   float percentage1 = (1024.0f-sensorValue1)/10.24;
//   float percentage2 = (1024.0f-sensorValue2)/10.24;
//   float percentage3 = (1024.0f-sensorValue3)/10.24;
//   float percentage4 = (1024.0f-sensorValue4)/10.24;
//   digitalWrite(power0, LOW);
//   digitalWrite(power1, LOW);
//   Serial.println("p " + String(percentage0, 6));
//   delay(1000);
//   Serial.println("cl " + String(percentage1, 6));
//   delay(1000);
//   Serial.println("pr " + String(percentage2, 6));
//   delay(1000);
//   Serial.println("cr " + String(percentage3, 6));
//   delay(1000);
//   Serial.println("pl " + String(percentage4, 6));
  
//   delay(1800000);
// }
#include <Arduino.h>
#include <stdio.h>

const int moistureSensor0 = A5;
const int moistureSensor1 = A6;
const int moistureSensor2 = A7;
const int power0 = 4;
const int power1 = 3;
const int power2 = 2;


void setup() {
  Serial.begin(9600);
  pinMode(power0, OUTPUT);
  pinMode(power1, OUTPUT); 
  pinMode(power2, OUTPUT); 
}

void loop() {
  digitalWrite(power0, HIGH);
  digitalWrite(power1, HIGH);
  digitalWrite(power2, HIGH);
  delay(1000);
  int sensorValue0 = analogRead(moistureSensor0);
  int sensorValue1 = analogRead(moistureSensor1);
  int sensorValue2 = analogRead(moistureSensor2);
  delay(1000);
  float percentage0 = (1024.0f-sensorValue0)/10.24;
  float percentage1 = (1024.0f-sensorValue1)/10.24;
  float percentage2 = (1024.0f-sensorValue2)/10.24;
  digitalWrite(power0, LOW);
  digitalWrite(power1, LOW);
  digitalWrite(power2, LOW);
  Serial.println("fpl " + String(percentage0, 6));
  delay(1000);
  Serial.println("fpr " + String(percentage1, 6));
  delay(1000);
  Serial.println("fc " + String(percentage2, 6));
  
  delay(1800000);
}