import RPi.GPIO as IoPort
import time

def KeyInput(key):
    if IoPort.input(key) == True:
        return False
    time.sleep(0.1)
    while True:
        if IoPort.input(key) == True:
            break
    time.sleep(0.1)
    return True

def time_sleep(Dly):
    global Work
    if KeyInput(Key2) == True:
        Work = False
        return
    time.sleep(Dly)

def Sig_a(Port1, Port2, Delay):
    if Work == False:
        return
    IoPort.output(Port1, False)
    IoPort.output(Port2, True)
    time.sleep(Delay)
    if Work == False:
        return
    IoPort.output(Port2, False)
    time_sleep(Delay)

def Sig_b(Port1, Port2, Delay):
    if Work == False:
        return
    IoPort.output(Port1, True)
    IoPort.output(Port2, True)
    time.sleep(Delay)
    if Work == False:
        return
    IoPort.output(Port2, False)
    time_sleep(Delay)

def Sig_c(Port1, Port2, Delay):
    if Work == False:
        return
    IoPort.output(Port1, True)
    IoPort.output(Port2, True)
    time.sleep(Delay)
    if Work == False:
        return
    IoPort.output(Port1, False)    
    IoPort.output(Port2, False)
    time_sleep(Delay)

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

Work = True
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
    if KeyInput(Key1) == False:
        continue
    Work = True
    Sig_a(Led, Clk, 0.4)
    Sig_a(Led, Clk, 0.4)
    Sig_a(Led, Clk, 0.4)
    Send_S(Led, Clk)
    Send_O(Led, Clk)
    Send_S(Led, Clk)    
    Sig_a(Led, Clk, 0.4)
    Sig_a(Led, Clk, 0.4)