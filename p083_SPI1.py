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

def Spi_out(bit, dly, sck):
    if bit == 1:
        IoPort.output(MOSI, True)
    else:
        IoPort.output(MOSI, False)
    sck(dly)

def Sck_a(dly):
    IoPort.output(SCK, False)
    time.sleep(dly)
    IoPort.output(SCK, True)
    time.sleep(2 * dly)
    IoPort.output(SCK, False)
    time.sleep(dly)

def Sck_b(dly):
    IoPort.output(SCK, True)
    time.sleep(dly)
    IoPort.output(SCK, False)
    time.sleep(2 * dly)
    IoPort.output(SCK, True)
    time.sleep(dly)

MOSI = 18
SCK = 23
Key1 = 21
Key2 = 19
IoPort.setmode(IoPort.BCM)
IoPort.setup(MOSI, IoPort.OUT)
IoPort.setup(SCK, IoPort.OUT)
IoPort.setup(Key1, IoPort.IN)
IoPort.setup(Key2, IoPort.IN)

while True:
    if KeyInput(Key1) == True:
        spi_c = Sck_a
    elif KeyInput(Key2) == True:
        spi_c = Sck_b
    else:
        continue # 둘다 뗴고 있으면(KeyInput때문에 반대가 됨) continue
    Spi_out(1, 0.2, spi_c)
    Spi_out(1, 0.2, spi_c)
    Spi_out(0, 0.2, spi_c)
    Spi_out(0, 0.2, spi_c)
    Spi_out(0, 0.2, spi_c)
    Spi_out(1, 0.2, spi_c)
    Spi_out(0, 0.2, spi_c)
    Spi_out(0, 0.2, spi_c)    