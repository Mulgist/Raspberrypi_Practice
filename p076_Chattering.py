import RPi.GPIO as IoPort
import time

def DisplayState(St):
    if St == 1:
        IoPort.output(Led1, False)
        IoPort.output(Led2, False)
    elif St == 2:
        IoPort.output(Led1, True)
        IoPort.output(Led2, False)
    elif St == 3:
        IoPort.output(Led1, False)
        IoPort.output(Led2, True)
    else:
        IoPort.output(Led1, True)
        IoPort.output(Led2, True)

Key1 = 21
Led1 = 18
Led2 = 23
IoPort.setmode(IoPort.BCM)
IoPort.setup(Led1, IoPort.OUT)
IoPort.setup(Led2, IoPort.OUT)
IoPort.setup(Key1, IoPort.IN)

State = 1
while State <= 4:
    DisplayState(State)
    while True:
        if IoPort.input(Key1) == False:
            break
    time.sleep(0.03)
    while True:
        if IoPort.input(Key1) == True:
            break
    time.sleep(0.03)
    State += 1
DisplayState(1)