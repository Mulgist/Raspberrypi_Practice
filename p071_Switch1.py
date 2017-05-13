import RPi.GPIO as IoPort

Sw1 = 21
Led = 18
IoPort.setmode(IoPort.BCM)
IoPort.setup(Led, IoPort.OUT)
IoPort.setup(Sw1, IoPort.IN)

while True:
    rcv = IoPort.input(Sw1)
    IoPort.output(Led, rcv)