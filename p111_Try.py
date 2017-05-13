while True:
    rcv = input('input no : ')
    try:
        ival = int(rcv)
        break
    except:
        print(rcv, ' is not integer no. try again!')
print('Receive No. is ', ival)