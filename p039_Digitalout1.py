import RPi.GPIO as IoPort
import time
IoPort.setmode(IoPort.BCM)
IoPort.setup(26, IoPort.OUT)

IoPort.output(26, True)
time.sleep(2)
IoPort.output(26, False)
