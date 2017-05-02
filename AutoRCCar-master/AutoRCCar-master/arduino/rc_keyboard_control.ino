// Motor 1 BACK MOTOR
int dir1PinA = 4;
int dir2PinA = 5;
int speedPinA = 3; // Needs to be a PWM pin to be able to control motor speed

// Motor 2 FRONT MOTOR
int dir1PinB = 6;
int dir2PinB = 7;
int speedPinB = 8; // Needs to be a PWM pin to be able to control motor speed


// duration for output
int time = 50;
// initial command
int command = 0;

void setup() {
pinMode(dir1PinA,OUTPUT);
pinMode(dir2PinA,OUTPUT);
pinMode(speedPinA,OUTPUT);
pinMode(dir1PinB,OUTPUT);
pinMode(dir2PinB,OUTPUT);
pinMode(speedPinB,OUTPUT);
}

void loop() {
  //receive command
  if (Serial.available() > 0){
    command = Serial.read();
  }
  else{
    reset();
  }
   send_command(command,time);
}

void right(int time){
Serial.println("Motor 2 Right");
analogWrite(speedPinB, 255);
digitalWrite(dir1PinB, HIGH);
digitalWrite(dir2PinB, LOW);
delay(time);

}

void left(int time){
Serial.println("Motor 2 Left");
analogWrite(speedPinB, 255);
digitalWrite(dir1PinB, LOW);
digitalWrite(dir2PinB, HIGH);
delay(time);
}

void forward(int time){
Serial.println("Motor 1 Forward"); // Prints out “Motor 1 Forward” on the serial monitor
analogWrite(speedPinA, 150);//Sets speed variable via PWM 
digitalWrite(dir1PinA, HIGH);
digitalWrite(dir2PinA, LOW); 
delay(time);
}

void reverse(int time) {
Serial.println("Motor 1 ");
analogWrite(speedPinA, 150);
digitalWrite(dir1PinA, LOW);
digitalWrite(dir2PinA, HIGH);
delay(time);
}

// void forward_right(int time){
//   digitalWrite(forward_pin, LOW);
//   digitalWrite(right_pin, LOW);
//   delay(time);
// }

// void reverse_right(int time){
//   digitalWrite(reverse_pin, LOW);
//   digitalWrite(right_pin, LOW);
//   delay(time);
// }

// void forward_left(int time){
//   digitalWrite(forward_pin, LOW);
//   digitalWrite(left_pin, LOW);
//   delay(time);
// }

// void reverse_left(int time){
//   digitalWrite(reverse_pin, LOW);
//   digitalWrite(left_pin, LOW);
//   delay(time);
// }

void reset(){
Serial.println("Motor 1 Stop");
digitalWrite(dir1PinA, LOW);
digitalWrite(dir2PinA, LOW);

Serial.println("Motor 2 Stop");
digitalWrite(dir1PinB, LOW);
digitalWrite(dir2PinB, LOW);
}

void send_command(int command, int time){
  switch (command){

     //reset command
     case 0: reset(); break;

     // single command
     case 1: forward(time); break;
     case 2: reverse(time); break;
     case 3: right(time); break;
     case 4: left(time); break;

     //combination command
//     case 6: forward_right(time); break;
//     case 7: forward_left(time); break;
//     case 8: reverse_right(time); break;
//     case 9: reverse_left(time); break;

     default: Serial.print("Inalid Command\n");
    }
}
