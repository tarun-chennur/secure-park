//Receiver Code

// Libraries
#include <ESP8266WiFi.h>
#include <RH_ASK.h>
#include <SPI.h>
#include "ESP_MICRO.h"

//RH_ASK driver(2000, 4, 5, 0); //ESP8266; bits/sec => 2000; Receive_Pin ->4 [D2] ; Transmit_Pin -> 5 [D1]

// SSID
const char* ssid     = "SSID Name";
const char* password = "SSID Password";
#define BUFSIZE 20
uint8_t UID[10];
int len=0;

void On() {
  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)  
}

void setup() {
  
  // Serial
  Serial.begin(115200);
  On();
  
  //Strting local server with DNS
  start(ssid,password);
}

void readfromSerial() {
  
  if(Serial.available()>0){
      len = Serial.available();
  
  for(int i=0;i<len;i++){
    UID[i]=Serial.read();
  }

  for(int i=len;i<10;i++){
    UID[i]=32;
  }
  
  Serial.println((char *)UID);  
  
  }
   
}
int var =0;

void loop() {

// readfromSerial();
   waitUntilNewReq();
   readfromSerial();
   returnThisStr((char *)UID);

   for(int i=0;i<10;i++){
    UID[i]=32;
  }
//   returnThisInt(var);
//   var += 1;  
   delay(1000); 
}
