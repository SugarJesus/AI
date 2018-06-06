#Жуков Василий ФИТ ИВТ 4 курс
import time
b=0
c="0"
n=""
test=input("test ")
if test == '1':
    b = 5
elif test == '2':
    b = 13
elif test == '3':
    b = 22
elif test == '4':
    b = 33
else:
    b=int(input())

while b > 1:
    y = str(b % 2)
    n = y + c + n
    b = int(b / 2)

l = list(n)
l.reverse()
l.append(1)
print(''.join(map(str, l)))
time.sleep(5)
