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

def GetKey(Key, St):
    if IoPort.input(Key) == True:
        return St
    time.sleep(0.05)
    while True:
        if IoPort.input(Key) == True:
            break
    time.sleep(0.05)
    return St + 1

Key1 = 21
Key2 = 19
Led1 = 18
Led2 = 23
IoPort.setmode(IoPort.BCM)
IoPort.setup(Led1, IoPort.OUT)
IoPort.setup(Led2, IoPort.OUT)
IoPort.setup(Key1, IoPort.IN)
IoPort.setup(Key2, IoPort.IN)

State = 1
while True:
    DisplayState(State)
    if State == 1:
        State = GetKey(Key1, State)
    elif State == 2:
        State = GetKey(Key1, State)
        if GetKey(Key2, 0) > 0:
            break
    elif State == 3:
        State = GetKey(Key1, State)
    else:
        State = GetKey(Key1, State)
        if GetKey(Key2, 0) > 0:
            break
    if State > 4:
        State = 1
DisplayState(State)