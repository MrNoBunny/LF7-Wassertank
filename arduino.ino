// Der Befehl, den der Pi an den Arduino sendet
String command;

// Pins der Sensoren
int tempPin = 0;
int waterPin = 1;

void setup() {
  // Serielle Schnittstelle konfigurieren
  Serial.begin(9600);
  // GPIO 13 wird als Ausgang verwendet
  pinMode(13, OUTPUT);
}

void loop() {
  // Auslesen des Temperatursensors und berechnen der Temperatur
  int tempReading = analogRead(tempPin);
  double tempK = log(10000.0 * ((1024.0 / tempReading - 1)));
  tempK = 1 / (0.001129148 + (0.000234125 + (0.0000000876741 * tempK * tempK )) * tempK );       //  Temp Kelvin
  float tempC = tempK - 273.15;            // Convert Kelvin to Celcius
  // Senden des Temperaturwertes
  Serial.print(tempC);
  Serial.print(", ");
  
  //Auslesen des Wassersensors
  int waterReading = analogRead(waterPin);
  //Senden des Wasserstandwertes
  Serial.print(waterReading);
  Serial.print("\n");

  // Empfang des Befehles des Pis
  if(Serial.available()){
    command = Serial.readStringUntil('\n');
    command.trim();
  // Befehlt bearbeiten
    if (command.equals ("HOT")){
      digitalWrite(13,HIGH);
    }else{
      digitalWrite(13,LOW) ;
    }
  }
delay(1000);
}
