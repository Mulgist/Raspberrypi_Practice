str1 = "ABC65.7abc"
print(str1.upper(), ',  ', str1.lower())
str2 = chr(65) + str(65)
print(str2, ' (', len(str2), ') ', str2[0], ', ', str2[1], ', ', str2[2])

for ch in str2:
    val1 = ord(ch)
    print(val1)
str3 = str1 + str2
print(str3)
strtst = 'name,home,year'
strs = strtst.split(',');
print(strs[0], ' ', strs[1], ' ', strs[2])

bts1 = b'12de'
bts2 = bytes(str2, 'UTF8')
bts3 = bts1 + bts2
btss = ''
for bs in bts3:
    btss += chr(bs)
print(bts3, ', ', btss)

str4 = str1[3:7]
fval = float(str4)
str4s = str(fval)
print(str4, ' : ', fval, ' : ', str4s)
str5 = str1[3:5]
ival1 = int(str5)
ival2 = int(fval)
ival = ival1 + ival2
str5s = str(ival) + chr(ival1)
print(str5, ' : ', ival, ' : ', str5s)