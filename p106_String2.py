ival = 65
fval = 34.5
ivals = hex(ival)
fvals = fval.hex()
print(ivals, ', ', fvals)

iv1 = int(ivals, base=16)
fv1 = float.fromhex(fvals)
print(iv1, ', ', fv1)

ival1 = 0x41
ival1s = bin(ival1)
ival2 = int(ival1s, base=2)
print(ival1, ', ', ival1s, ', ', ival2)

ival3 = 0b01000001
ival3s = bin(ival3)
print(ival3, ', ', ival3s)