#Жуков Василий ФИТ ИВТ 4 курс
#21.06 - 1.32
import time
b = 0
l=[]
test=input("test ")
if test == '1':
    b = 5
elif test == '2':
    b = 25
elif test == '3':
    b = 100
elif test == '4':
    b = 1000
else:
    b=int(input())

if 1 <= b <= 8:
    b = b - 1
    l=['0']
    if b == 0:
        l=l+['000']
    elif b == 1:
        l=l+['00']
    elif 2 <= b <= 3:
        l=l+['0']
    else:
        l=l
elif 9 <= b <= 40:
    b = b - 9
    l=['10']
    if b == 0:
        l=l+['00000']
    elif b == 1:
        l=l+['0000']
    elif 2 <= b <= 3:
        l=l+['000']
    elif 4 <= b <= 7:
        l=l+['00']
    elif 8 <= b <= 15:
        l=l+['0']
    else:
        l=l
elif 41 <= b <= 168:
    b = b - 41
    l=['110']
    if b == 0:
        l=l+['000000']
    elif b == 1:
        l=l+['00000']
    elif 2 <= b <= 3:
        l=l+['0000']
    elif 4 <= b <= 7:
        l=l+['000']
    elif 8 <= b <= 15:
        l=l+['00']
    elif 16 <= b <= 31:
        l=l+['0']
    else:
        l=l
elif 169 <= b <= 680:
    b = b - 169
    l=['1110']
    if b == 0:
        l=l+['000000000']
    elif b == 1:
        l=l+['00000000']
    elif 2 <= b <= 3:
        l=l+['0000000']
    elif 4 <= b <= 7:
        l=l+['000000']
    elif 8 <= b <= 15:
        l=l+['00000']
    elif 16 <= b <= 31:
        l=l+['0000']
    elif 32 <= b <= 63:
        l=l+['000']
    elif 64 <= b <= 127:
        l=l+['00']
    elif 128 <= b <= 255:
        l=l+['0']
    else:
        l=l
elif 681 <= b <= 2728:
    b = b - 681
    l=['1111']
    if b == 0:
        l=l+['00000000000']
    elif b == 1:
        l=l+['0000000000']
    elif 2 <= b <= 3:
        l=l+['000000000']
    elif 4 <= b <= 7:
        l=l+['00000000']
    elif 8 <= b <= 15:
        l=l+['0000000']
    elif 16 <= b <= 31:
        l=l+['000000']
    elif 32 <= b <= 63:
        l=l+['00000']
    elif 64 <= b <= 127:
        l=l+['0000']
    elif 128 <= b <= 255:
        l=l+['000']
    elif 256 <= b <= 511:
        l=l+['00']
    elif 512 <= b <= 1023:
        l=l+['0']
    else:
        l=l
else:
    print('error')

n = ""
while b > 0:
    y = str(b % 2)
    n = y + n
    b = int(b / 2)

l.extend(n)
print(''.join(l))
time.sleep(5)
