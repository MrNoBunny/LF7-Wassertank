// Wassertank 

// Variable für Befehl, den der Pi an den Arduino sendet
String command;

// Pins für die Pumpen definieren
int pumpe1Pin = 2;
int pumpe2Pin = 13;

// Code-Bibliothek für das LCD
#include <LiquidCrystal.h>
// LCD initialisieren, mit den Nummern der Interface-Pins
LiquidCrystal lcd(7, 8, 6, 5, 4, 3);

// Code-Bibliothek für Ultraschall-Entfernungsmessung
#include <SR04.h>
// Definieren der Pins und initialisien der Ultraschall-Entfernungsmessung
#define TRIG_PIN1 12
#define ECHO_PIN1 11
#define TRIG_PIN2 9
#define ECHO_PIN2 10
SR04 tank1 = SR04(ECHO_PIN1,TRIG_PIN1);
SR04 tank2 = SR04(ECHO_PIN2,TRIG_PIN2);
long abstand1;
long abstand2;
long wasserstand1;
long wasserstand2;


void setup() {
  // Pins für die Pumpen initialisieren
  pinMode(pumpe1Pin, OUTPUT);
  pinMode(pumpe2Pin, OUTPUT);
  // Anzahl der Spalten und Zeilen des LCD festlegen
  lcd.begin(16, 2);
  // Ausgabe auf LCD
  lcd.print("Wasserstand:");
  // Serial-Ausgabe aktivieren
  Serial.begin(9600);
  delay(1000);
}

void loop() {
  // Abstand messen
  abstand1=tank1.Distance();
  abstand2=tank2.Distance();

  // Wasserstand berechnen
  wasserstand1=10-abstand1;
  wasserstand2=10-abstand2;
  
  // Serial-Ausgabe
  Serial.print(wasserstand1);
  Serial.print(", ");
  Serial.print(wasserstand2);
  Serial.print(", ");
  Serial.print(abstand1);
  Serial.print(", ");
  Serial.print(abstand2);
  Serial.print("\n");
  
  // LCD-Anzeige
  // Cursor auf Spalte 0, Zeile 1 setzen
  // (Hinweis: Zeile 1 ist die zweite Zeile, da bei 0 begonnen wird zu zählen):
  lcd.setCursor(0, 1);
  // Inhalt der Zeile löschen
  for(int n = 0; n < 16; n++) {
    lcd.print(" ");
  }
  // Wasserstand anzeigen
  // Tank 1 in der ersten Hälfte der zweiten Zeile
  lcd.setCursor(0, 1);
  lcd.print(wasserstand1);
  lcd.print("cm");
  // Tank 2 in der zweiten Hälfte der zweiten Zeile
  lcd.setCursor(7, 1);
  lcd.print("| ");
  lcd.print(wasserstand2);
  lcd.print("cm");

  // Empfang von Befehlen des Pis
  if(Serial.available()){
    command = Serial.readStringUntil('\n');
    command.trim();
  // Befehl bearbeiten (pumpen)
    if (command.equals("PUMPEN_1")){
      digitalWrite(pumpe1Pin,HIGH);
    }else{
      digitalWrite(pumpe1Pin,LOW) ;
    }
    if (command.equals("PUMPEN_2")){
      digitalWrite(pumpe2Pin,HIGH);
    }else{
      digitalWrite(pumpe2Pin,LOW) ;
    }
  }
  delay(1000);
}
