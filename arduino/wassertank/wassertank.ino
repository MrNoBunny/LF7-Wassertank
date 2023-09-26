// Wassertank 

// Der Befehl, den der Pi an den Arduino sendet
String command;

// pin for water sensor
int waterPin = 1;

// include the LCD library code:
#include <LiquidCrystal.h>
// initialize the LCD library with the numbers of the interface pins
LiquidCrystal lcd(7, 8, 6, 5, 4, 3);

// include Ultrasonic Distance Measurement library
#include <SR04.h>
// define the pins and initialize the Ultrasonic Distance Measurement library
#define TRIG_PIN 12
#define ECHO_PIN 11
SR04 sr04 = SR04(ECHO_PIN,TRIG_PIN);
long abstand;


void setup() {
  // setup LED pin
  pinMode(13, OUTPUT);
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // Print a message to the LCD.
  lcd.print("Wasserstand:");
  // enable serial output
  Serial.begin(9600);
  delay(1000);
}

void loop() {
  //Auslesen des Wassersensors
  int waterReading = analogRead(waterPin);

  //measure the distance
  abstand=sr04.Distance();
  
  // write serial output
  Serial.print(waterReading);
  Serial.print(", ");
  Serial.print(abstand);
  Serial.print("\n");
  
  // Write LCD Output
  // set the cursor to column 0, line 1
  // (note: line 1 is the second row, since counting begins with 0):
  lcd.setCursor(0, 1);
  //clear the line
  for(int n = 0; n < 16; n++) {
    lcd.print(" ");
  }
  // print the distance
  lcd.setCursor(0, 1);
  lcd.print(abstand);
  lcd.print(" cm");

  // Empfang des Befehles des Pis
  if(Serial.available()){
    command = Serial.readStringUntil('\n');
    command.trim();
  // Befehlt bearbeiten
    if (command.equals("WARNING")){
      digitalWrite(13,HIGH);
    }else{
      digitalWrite(13,LOW) ;
    }
  }
  delay(1000);
}

