import RPi.GPIO as IoPort
import time

Led = 18
IoPort.setmode(IoPort.BCM)
IoPort.setup(Led, IoPort.OUT)

# 대기
IoPort.output(Led, False)
time.sleep(2.4)

# S 출력
IoPort.output(Led, True)
time.sleep(0.4)
IoPort.output(Led, False)
time.sleep(0.4)
IoPort.output(Led, True)
time.sleep(0.4)
IoPort.output(Led, False)
time.sleep(0.4)
IoPort.output(Led, True)
time.sleep(0.4)
IoPort.output(Led, False)
time.sleep(1.2)

# O 출력
IoPort.output(Led, True)
time.sleep(1.2)
IoPort.output(Led, False)
time.sleep(0.4)
IoPort.output(Led, True)
time.sleep(1.2)
IoPort.output(Led, False)
time.sleep(0.4)
IoPort.output(Led, True)
time.sleep(1.2)
IoPort.output(Led, False)
time.sleep(1.2)

# O 출력
IoPort.output(Led, True)
time.sleep(0.4)
IoPort.output(Led, False)
time.sleep(0.4)
IoPort.output(Led, True)
time.sleep(0.4)
IoPort.output(Led, False)
time.sleep(0.4)
IoPort.output(Led, True)
time.sleep(0.4)
IoPort.output(Led, False)
time.sleep(1.2)