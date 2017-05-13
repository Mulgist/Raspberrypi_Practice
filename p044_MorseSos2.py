import RPi.GPIO as IoPort
import time

def LedOn(Port, Delay) :
    IoPort.output(Port, True)
    time.sleep(Delay);

def LedOff(Port, Delay) :
    IoPort.output(Port, False)
    time.sleep(Delay)

Led = 18
IoPort.setmode(IoPort.BCM)
IoPort.setup(Led, IoPort.OUT)
LedOff(Led, 2.4)

# S 출력
LedOn(Led, 0.4)
LedOff(Led, 0.4)
LedOn(Led, 0.4)
LedOff(Led, 0.4)
LedOn(Led, 0.4)
LedOff(Led, 1.2)

# O 출력
LedOn(Led, 1.2)
LedOff(Led, 0.4)
LedOn(Led, 1.2)
LedOff(Led, 0.4)
LedOn(Led, 1.2)
LedOff(Led, 1.2)

# S 출력
LedOn(Led, 0.4)
LedOff(Led, 0.4)
LedOn(Led, 0.4)
LedOff(Led, 0.4)
LedOn(Led, 0.4)
LedOff(Led, 1.2)