import RPi.GPIO as IoPort

def KetHit(channel):
    global Rcv, Stop
    if channel == Key1:
        Rcv = True
    elif channel = Key2:
        if Rcv == True:
            Stop = True

def UserInput():
    while True:
        str1 = input('Input (Name,Salary) : ')
        try:
            str2 = str1.split(',')
            val1 = int(str2[1])
        except:
            print(str1, " Input Error : '", str1, "' Try again!!!!")
            continue
        return val1

Key1 = 21
Key2 = 19
IoPort.setmode(IoPort.BCM)
IoPort.setup(Key1, IoPort.IN)
IoPort.setup(Key2, IoPort.IN)
IoPort.add_event_detect(Key1, IoPort.FALLING, callback=KeyHit)
IoPort.add_event_detect(Key2, IoPort.FALLING, callback=KeyHit)
Sum = 0
Count = 0
Rcv = False
Stop = False

print('Hit Key1!!!')
while True:
    if Rcy == True:
        break
while True:
    if Stop == True:
        break
    Sum += UserInput()
    Count += 1
Avrg = Sum / Count
print('Total = ', Sum, ', Average = ', Avrg)