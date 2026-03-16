#define NANO

#ifdef NANO
  #define PIN_R A1
  #define PIN_L A2
  #define PIN_B A3
  #define PIN_F A4
#else  // PICO
  #define PIN_R 1
  #define PIN_L 2
  #define PIN_B 3
  #define PIN_F 4
#endif

#define N_PINS 4
uint8_t CONTROL_PINS[N_PINS] = {PIN_F, PIN_R, PIN_B, PIN_L};

#define DEFAULT_ON_TIME_MS 200
uint16_t DEFAULT_ON_TIMES_MS[N_PINS] = {DEFAULT_ON_TIME_MS};

float MULT = 1;

int64_t NEXT_OFF_TIMES[N_PINS] = {-1};


void setup() {
  for (int i = 0; i < N_PINS; i++) {
    pinMode(CONTROL_PINS[i], OUTPUT);
    digitalWrite(CONTROL_PINS[i], HIGH);
  }

  Serial.begin(115200);  
}

void loop() {
  for (int i = 0; i < N_PINS; i++) {
    int64_t next_off_time = NEXT_OFF_TIMES[i];
    if (next_off_time >= 0 && ((int64_t)millis()) > next_off_time) {
      digitalWrite(CONTROL_PINS[i], HIGH);
      NEXT_OFF_TIMES[i] = -1;
    }
  }

  if (Serial.available()) {
    String s = Serial.readStringUntil('\n');
    if (s.length() == 0) {
      return;
    }

    if (s.startsWith("press")) {
      // parse into pairs press_[pin]-[ms]_[pin]-[ms]
      s = s.substring(6);
      String ss;
      for (int i = 0; i < N_PINS; i++) {
        int index = s.indexOf('_');
        if (index >= 0) {
          ss = s.substring(0, index);
          s = s.substring(index+1);
        } else {
          ss = s;
          s = "";
        }

        index = ss.indexOf('-');
        if (index >= 0) {
          int pinNumber = ss.substring(0, index).toInt();
          int delayMs = ss.substring(index+1).toInt();

          if (pinNumber > 0 && pinNumber <= N_PINS) {
            if (delayMs > 0 && delayMs <= 60000) {
              digitalWrite(CONTROL_PINS[pinNumber-1], LOW);
              uint32_t next_off_time = millis() + (delayMs * MULT);  // keep it positive even though we store in signed 64
              NEXT_OFF_TIMES[pinNumber-1] = next_off_time;
            } else if (delayMs == -1) {  // on indefinitely
              digitalWrite(CONTROL_PINS[pinNumber-1], LOW);
              NEXT_OFF_TIMES[pinNumber-1] = -1;
            }
          }
        }
      }
    } else if (s.startsWith("mult")) {
      // parse into mult_[float]
      s = s.substring(5);
      MULT = s.toFloat();
      if (MULT <= 0 || MULT > 100) {
        MULT = 1;
      }
    } else if (s.startsWith("release")) {
      // parse into release_[pin]_[pin]...
      s = s.substring(8);
      String ss;
      for (int i = 0; i < N_PINS; i++) {
        int index = s.indexOf('_');
        if (index >= 0) {
          ss = s.substring(0, index);
          s = s.substring(index+1);
        } else {
          ss = s;
          s = "";
        }

        if (ss.length() > 0) {
          int pinNumber = ss.substring(0, index).toInt();

          if (pinNumber > 0 && pinNumber <= N_PINS) {
              digitalWrite(CONTROL_PINS[pinNumber-1], HIGH);
          }
        }
      }
    }
  }
}
