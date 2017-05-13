import RPi.GPIO as IoPort
import time

Led = 22
IoPort.setmode(IoPort.BCM)
IoPort.setup(Led, IoPort.OUT)
IoPort.output(Led, True)
time.sleep(2)
IoPort.output(Led, False)
