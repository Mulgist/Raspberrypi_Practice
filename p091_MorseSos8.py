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

def Pulse_a(Prt, Dly):
    IoPort.output(Prt, True)
    time.sleep(Dly)
    IoPort.output(Prt, False)
    time.sleep(Dly)

def Pulse_A(Prt, Dly):
    IoPort.output(Prt, True)
    time.sleep(Dly/2)
    IoPort.output(Prt, False)
    time.sleep(Dly/2)
    IoPort.output(Prt, True)
    time.sleep(Dly/2)
    IoPort.output(Prt, False)
    time.sleep(Dly/2)

def Pulse_c(Prt1, Prt2, Dly):
    IoPort.output(Prt2, True)
    time.sleep(Dly)
    IoPort.output(Prt1, False)
    IoPort.output(Prt2, False)
    time.sleep(Dly)

def Pulse_C(Prt1, Prt2, Dly):
    IoPort.output(Prt2, True)
    time.sleep(Dly/2)
    IoPort.output(Prt2, False)
    time.sleep(Dly/2)
    IoPort.output(Prt1, False)
    IoPort.output(Prt2, True)
    time.sleep(Dly/2)
    IoPort.output(Prt2, False)
    time.sleep(Dly/2)

def Sig_a(Port1, Port2, Delay):
    IoPort.output(Port1, False)
    PlsA(Port2, Delay)

def Sig_b(Port1, Port2, Delay):
    IoPort.output(Port1, True)
    PlsA(Port2, Delay)

def Sig_c(Port1, Port2, Delay):
    IoPort.output(Port1, True)
    PlsC(Port1, Port2, Delay)

def Send_S(Port1, Port2):
    Sig_c(Port1, Port2, 0.4)
    Sig_c(Port1, Port2, 0.4)
    Sig_c(Port1, Port2, 0.4)
    Sig_a(Port1, Port2, 0.4)
    
def Send_O(Port1, Port2):
    Sig_b(Port1, Port2, 0.4)
    Sig_c(Port1, Port2, 0.4)
    Sig_b(Port1, Port2, 0.4)
    Sig_c(Port1, Port2, 0.4)
    Sig_b(Port1, Port2, 0.4)
    Sig_c(Port1, Port2, 0.4)
    Sig_a(Port1, Port2, 0.4)

PlsA = Pulse_a
PlsC = Pulse_c
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
        PlsA = Pulse_a
        PlsC = Pulse_c
    elif KeyInput(Key2) == True:
        PlsA = Pulse_A
        PlsC = Pulse_C
    else:
        continue
    Sig_a(Led, Clk, 0.4)
    Sig_a(Led, Clk, 0.4)
    Sig_a(Led, Clk, 0.4)
    Send_S(Led, Clk)
    Send_O(Led, Clk)
    Send_S(Led, Clk)
    Sig_a(Led, Clk, 0.4)
    Sig_a(Led, Clk, 0.4)