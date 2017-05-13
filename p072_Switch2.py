import RPi.GPIO as IoPort

Sw1 = 21
End = 19
Led = 18
IoPort.setmode(IoPort.BCM)
IoPort.setup(Led, IoPort.OUT)
IoPort.setup(End, IoPort.IN)
IoPort.setup(Sw1, IoPort.IN)

Count = 0
while Count == 0:
    rcv = IoPort.input(Sw1)
    if IoPort.input(End) == False:
        Count = 1
    IoPort.output(Led, rcv)
IoPort.output(Led, False)