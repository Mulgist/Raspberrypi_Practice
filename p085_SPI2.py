import RPi.GPIO as IoPort
import time

# 이벤트 실습
def KeyHit(channel):
    global spi_c
    if channel == Key1:
        spi_c = Sck_a
    elif channel == Key2:
        spi_c = Sck_b

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

IoPort.add_event_detect(Key1, IoPort.FALLING, callback=KeyHit)
IoPort.add_event_detect(Key2, IoPort.FALLING, callback=KeyHit)

spi_c = None

while True:
    if spi_c == None:
        continue
    Spi_out(1, 0.2, spi_c)
    Spi_out(1, 0.2, spi_c)
    Spi_out(0, 0.2, spi_c)
    Spi_out(0, 0.2, spi_c)
    Spi_out(0, 0.2, spi_c)
    Spi_out(1, 0.2, spi_c)
    Spi_out(0, 0.2, spi_c)
    Spi_out(0, 0.2, spi_c)
    spi_c = None