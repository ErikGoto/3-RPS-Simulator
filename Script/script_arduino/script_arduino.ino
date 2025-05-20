#include <Servo.h>

String inputString = "";
int angulo_1, angulo_2, angulo_3, angulo_4;

Servo servo_1;
Servo servo_2;
Servo servo_3;

void setup() {
  Serial.begin(115200);
  inputString.reserve(50);  // Reserva memória para a string recebida

  servo_1.attach(3);
  servo_2.attach(5);
  servo_3.attach(6);

  servo_1.write(180);
  servo_2.write(180);
  servo_3.write(180);
}

void loop() {
  if (Serial.available()) {
    char c = Serial.read();

    if (c == '\n') {
      // Quando receber o final da string, processa
      processaMensagem(inputString);
      // Clean a variável
      inputString = "";  
    } else {
      inputString += c;
    }

    // Define limites para o movimento dos braços
    if (angulo_1 >=130){
      servo_1.write(angulo_1);
    }
    if (angulo_2 >=130){
      servo_2.write(angulo_2);
    }
    if (angulo_3 >=130){
      servo_3.write(angulo_3);
    }
  }
}

void processaMensagem(String dados) {
  int sep1 = dados.indexOf(';');
  int sep2 = dados.indexOf(';', sep1 + 1);
  int sep3 = dados.indexOf(';', sep2 + 1);

  if (sep1 == -1 || sep2 == -1 || sep3 == -1) {
    Serial.println("Erro: formato inválido");
    return;
  }

  angulo_1 = dados.substring(0, sep1).toInt();
  angulo_2 = dados.substring(sep1 + 1, sep2).toInt();
  angulo_3 = dados.substring(sep2 + 1, sep3).toInt();
  angulo_4 = dados.substring(sep3 + 1).toInt();
}