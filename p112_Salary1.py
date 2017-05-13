def UserInput():
    while True:
        str1 = input('Input (Name,Salar) : ')
        try:
            str2 = str1.split(',')
            val1 = int(str2[1])
        except:
            print(str1, " Input Error : '", str1, "' Try again!!!!")
            continue
        return val1

Sum = 0
for i in range(0, 5):
    Sum += UserInput()
Avrg = Sum / 5.0
print('Total = ', Sum, ', Average = ', Avrg)