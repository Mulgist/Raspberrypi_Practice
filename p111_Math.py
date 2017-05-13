import math as Math
rcv = input('input real no : ')
frcv = float(rcv)
ircv = int(frcv)
print(' Receive Value = ', rcv, 
    '\n float value = ', frcv, 
    '\n integer value = ', ircv)
print('sqrt(', frcv, ') = ', Math.sqrt(frcv), 
    '\nSin(', frcv, ') = ', Math.sin(Math.radians(frcv)),
    '\nlog10(', ircv, ') = ', Math.log10(ircv))