#define NANO

#ifdef NANO
  #define PIN_R A1
  #define PIN_L A2
  #define PIN_B A3
  #define PIN_F A4
#else
  #define PIN_R 1
  #define PIN_L 2
  #define PIN_B 3
  #define PIN_F 4
#endif



void setup() {
  pinMode(PIN_R, OUTPUT);
  pinMode(PIN_L, OUTPUT);
  pinMode(PIN_B, OUTPUT);
  pinMode(PIN_F, OUTPUT);

  digitalWrite(PIN_R, HIGH);
  digitalWrite(PIN_L, HIGH);
  digitalWrite(PIN_B, HIGH);
  digitalWrite(PIN_F, HIGH);

  Serial.begin(115200);
  
}

int64_t next_off_time = -1;
#define DEFAULT_ON_TIME_MS 200

void loop() {
  if (next_off_time >= 0 && ((int64_t)millis()) > next_off_time) {
    digitalWrite(PIN_R, HIGH);
    digitalWrite(PIN_L, HIGH);
    digitalWrite(PIN_B, HIGH);
    digitalWrite(PIN_F, HIGH);
    next_off_time = -1;
  }

  if (Serial.available()) {
    String s = Serial.readStringUntil('\n');
    if (s.length() == 0) {
      return;
    }

    if (s.startsWith("r")) {
      digitalWrite(PIN_R, LOW);
      Serial.println("R");
      next_off_time = millis() + DEFAULT_ON_TIME_MS;
    } else if (s.startsWith("l")) {
      digitalWrite(PIN_L, LOW);
      Serial.println("L");
      next_off_time = millis() + DEFAULT_ON_TIME_MS;
    } else if (s.startsWith("b")) {
      digitalWrite(PIN_B, LOW);
      Serial.println("B");
      next_off_time = millis() + DEFAULT_ON_TIME_MS;
    } else if (s.startsWith("f")) {
      digitalWrite(PIN_F, LOW);
      Serial.println("F");
      next_off_time = millis() + DEFAULT_ON_TIME_MS;
    } else {
      digitalWrite(PIN_F, HIGH);
      Serial.println("Clear");
    }
  }
}
