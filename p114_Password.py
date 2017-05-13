import RPi.GPIO as IoPort
import time

def KeyHit(channel):
    global Stop
    if channel == Key1:
        if Stop == False:
            reutrn
        ChangePass()
        IoPort.output(Led, False)
    Stop = False

def BadWord():
    IoPort.output(Led, True)
    time.sleep(0.2)
    IoPort.output(Led, False)
    time.sleep(0.2)
    IoPort.output(Led, True)
    time.sleep(0.2)
    IoPort.output(Led, False)
    time.sleep(0.2)

def ChangePass():
    global Password
    while True:
        rcv1 = input('Input New Password : ')
        if len(rcv1) < 4:
            print('length of Password is too small. Try again!')
            continue
        if len(rcv1) > 8:
             print('length of Password is too big. Try again!')
            continue
        rcv2 = input('Input New Password again : ')
        if rcv1 != rcv2:
            print('password not match! Try again')
        else:
            Password = rcv1
            return

Led = 18
Key1 = 21
Key2 = 19
IoPort.setmode(IoPort.BCM)
IoPort.setup(Led, IoPort.OUT)
IoPort.setup(Key1, IoPort.IN)
IoPort.setup(Key2, IoPort.IN)
IoPort.add_event_detect(Key1, IoPort.FALLING, callback=KeyHit)
IoPort.add_event_detect(Key2, IoPort.FALLING, callback=KeyHit)
Password = '1234'
Rcv = False
Stop = False
IoPort.output(Led, False)

while True:
    if Stop == True:
        continue
    IoPort.output(Led, False)
    rcvstr = input('input Password : ')
    if rcvstr == Password:
        IoPort.output(Led, True)
        Stop = True
    else:
        BadWord()