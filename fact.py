#Жуков Василий ФИТ ИВТ 4 курс
#19.03 - 20.05 21.10-21.20
import time
x = 0
n = 2
b = 0
a = []
test=input("test ")
if test == '1':
    x = 47
elif test == '2':
    x = 83
elif test == '3':
    x = 100
elif test == '4':
    x = 213
else:
    x=int(input())
while x >= n:
    b = x%n
    x = x//n
    n = n+1
    a.append(b)
else:
    a.append(x)
    a.reverse()
print(''.join(map(str, a)))
time.sleep(5)
