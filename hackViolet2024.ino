//MIC
//Assign to pin A2:
//Jiyoon needs to change this probably:
int sound_sensor = 12;

int soundValue = 0;

int cyclesToLower = 0;

//Only needs to go up to 10
//checks for false alarms
int alarmLevel = 0;

//How loud it should be to set off the alarm
unsigned int worryNoise = 0;

//Is there an alarm?
bool isAlarm = false;


//LED
int led = 14;
//motor
int motor = 27;


void setup() {
  //How Loud Things Are:
  Serial.begin(9600); //begin Serial Communication
  //setting led pin as output:
  pinMode(led, OUTPUT);
  pinMode(motor, OUTPUT);
}
 
void loop(){  
  soundValue = analogRead(sound_sensor);
  
  Serial.println(soundValue); 
  isAlarm = signalProcessing();
  


  if(isAlarm == true){
    sendOutAlarm();
    digitalWrite(led, HIGH);
    digitalWrite(motor, HIGH);
    delay(500);
    digitalWrite(led, LOW);
    digitalWrite(motor, LOW);
    delay(500);
  }

  Serial.println(isAlarm);
  


  delay(100); 

  if(cyclesToLower == 3){
    cyclesToLower = 0;
    if(alarmLevel >= 0){
      alarmLevel--;
    }
  }else{
    //alarm level goes down, slower
    //only to 0
    cyclesToLower++;
  }
}

bool signalProcessing(){
  if(isAlarm == true){
    //if it's true, we want it to stay true until otherwise
    return true;
  }
  if(soundValue > 400){
    //increases alarm level
    if(alarmLevel < 10){
      //we want it to tick up faster, as false alarms are better than false quiets
      alarmLevel = alarmLevel + 2;
      return false;
    }
    //if it's at 10, return true
    if(alarmLevel == 10){
      return true;
    }
  }
}

void slowEnd(){

}

void sendOutAlarm(){
  //communicates to server over wifi

}

bool allClear(){
  //goes off when all clear signal does
  isAlarm = false;
}