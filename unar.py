#Жуков Василий ФИТ ИВТ 4 курс
#19.30 - 21.06
import time
b = 0
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
l = [c * b for c in '1'] + ['0']
print(''.join(l))
q=input("")
if q == 'q':
    exit()
