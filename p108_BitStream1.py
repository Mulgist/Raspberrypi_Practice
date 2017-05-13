import RPi.GPIO as IoPort
import time

def getbinary(dgt):
    bstr1 = bin(dgt)
    bstr2 = ''
    for i in range(2, len(bstr1)):
        bstr2 += bstr1[i]
    while len(bstr2) < 8:
        bstr2 = '0' + bstr2
    return bstr2

Led1 = 18
Led2 = 23
IoPort.setmode(IoPort.BCM)
IoPort.setup(Led1, IoPort.OUT)
IoPort.setup(Led2, IoPort.OUT)

while True:
    Rcv = input('Input String : ')
    for ch in Rcv:
        ival = ord(ch)
        bstr = getbinary(ival)
        print(ival, bstr)
        for i in range(0, 8):
            bt = bstr[7 - i]
            if bt == '1':
                IoPort.output(Led1, True)
            else:
                IoPort.output(Led1, False)
            IoPort.output(Led2, True)
            time.sleep(0.2)
            IoPort.output(Led2, False)
            time.sleep(0.2)