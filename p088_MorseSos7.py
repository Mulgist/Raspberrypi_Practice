import RPi.GPIO as IoPort
import time

def KeyInput(key):
    if IoPort.input(key) == True:   # 떼어짐
        return False                # 떼어지면 False
    time.sleep(0.1)
    while True:
        if IoPort.input(key) == True:   # 떼어짐
            break                       # 떼어지면 loop빠져나감
    time.sleep(0.1)
    return True # loop 빠져나가고 True

def Sig_a(Port1, Port2, Delay) :
    IoPort.output(Port1, False)
    IoPort.output(Port2, True)
    time.sleep(Delay)
    IoPort.output(Port2, False)
    time.sleep(Delay)

def Sig_b(Port1, Port2, Delay) :
    IoPort.output(Port1, True)
    IoPort.output(Port2, True)
    time.sleep(Delay)
    IoPort.output(Port2, False)
    time.sleep(Delay)

def Sig_c(Port1, Port2, Delay) :
    IoPort.output(Port1, True)
    IoPort.output(Port2, True)
    time.sleep(Delay)
    IoPort.output(Port1, False)
    IoPort.output(Port2, False)
    time.sleep(Delay)

def Send_S(Port1, Port2) :
    Sig_c(Port1, Port2, T04)
    Sig_c(Port1, Port2, T04)
    Sig_c(Port1, Port2, T04)
    Sig_a(Port1, Port2, T04)

def Send_O(Port1, Port2) :
    Sig_b(Port1, Port2, T04)
    Sig_c(Port1, Port2, T04)
    Sig_b(Port1, Port2, T04)
    Sig_c(Port1, Port2, T04)
    Sig_b(Port1, Port2, T04)
    Sig_c(Port1, Port2, T04)
    Sig_a(Port1, Port2, T04)

T04 = 0.2
Led = 18
Clk = 23
Key1 = 21
Key2 = 19
IoPort.setmode(IoPort.BCM)
IoPort.setup(Led, IoPort.OUT)
IoPort.setup(Clk, IoPort.OUT)
IoPort.setup(Key1, IoPort.IN)
IoPort.setup(Key2, IoPort.IN)

while True:
    if KeyInput(Key1) == True:
        T04 = 0.4
        break
    elif KeyInput(Key2) == True:
        T04 = 0.2
        break
    else:
        continue

Sig_a(Led, Clk, T04)
Sig_a(Led, Clk, T04)
Sig_a(Led, Clk, T04)

Send_S(Led, Clk)
Send_O(Led, Clk)
Send_S(Led, Clk)

Sig_a(Led, Clk, T04)
Sig_a(Led, Clk, T04)