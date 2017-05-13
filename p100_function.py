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

def Multi(val, fnc):
    return fnc(val)

def Adder(val, adv):
    return adv(val)

def mul2(val):
    return val * 2

def mul3(val):
    return val * 3

def add3(val):
    return val + 3

def add7(val):
    return val + 7

key1 = 21
key2 = 7
IoPort.setmode(IoPort.BCM)
IoPort.setup(key1, IoPort.IN)
IoPort.setup(key2, IoPort.IN)

while True:
    rcv = input("Input Number : ")
    if rcv.isdigit() == False:
        print(rcv, ' is not a Number!, Try Again!!!')
        continue
    val = int(rcv)
    while True:
        if KeyInput(key1) == True:
            val = Multi(val, mul2)
            func = add3
            break
        if KeyInput(key2) == True:
            val = Multi(val, mul3)
            func = add7
            break
    print('Result = ', Adder(val, func))