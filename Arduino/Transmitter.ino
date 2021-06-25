#include<RH_ASK.h>
#ifdef RH_HAVE_HARDWARE_SPI
#include<SPI.h> 
#endif

int times=0;

//RH_ASK driver;
RH_ASK driver(2000, 4, 5, 0);  //ESP8266; bits/sec => 2000; Receive_Pin ->4 [D2] ; Transmit_Pin -> 5 [D1]

void setup() {
  
  pinMode(LED_BUILTIN, OUTPUT);
  
  #ifdef RH_HAVE_SERIAL
    Serial.begin(9600);
  #endif

  if(!driver.init()){
    #ifdef RH_HAVE_SERIAL
    Serial.println("init failed");
    #else
    ;
    #endif
  }
  
  
}

void blink() {
  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(3000);                       // wait for a second
  digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
  delay(3000);                       // wait for a second
}

void loop() {
  const char *msg = "Hello";
  blink();

  driver.send((uint8_t *)msg, strlen(msg));
  driver.waitPacketSent(); //wait till the all the packets are sent 
 
  Serial.print("Hello sent"); //Debugging purpose only 
  times += 1;
  Serial.print(times);
  Serial.print("\n");
  
  delay(1000); //Sending message every 1000ms or 1 second
  
}
