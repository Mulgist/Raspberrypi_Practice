import RPi.GPIO as IoPort
import time

def DisplayState(Ld1, Ld2):
    IoPort.output(Led1, Ld1)
    IoPort.output(Led2, Ld2)

def StateWork(St):
    if St == 1:
        return False, False
    elif St == 2:
        return True, False
    elif St == 3:
        return False, True
    else:
        return True, True
    
Led1 = 18
Led2 = 23
IoPort.setmode(IoPort.BCM)
IoPort.setup(Led1, IoPort.OUT)
IoPort.setup(Led2, IoPort.OUT)

State = 1
while True:
    Ld1, Ld2 = StateWork(State)
    DisplayState(Ld1, Ld2)
    State += 1
    time.sleep(0.4)
    if State > 4:
        State = 1