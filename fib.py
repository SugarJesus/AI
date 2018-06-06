#Жуков Василий ФИТ ИВТ 4 курс
#21.23-22.22
import time
fib1 = 1
fib2 = 1
a = [1, 1]
b = []
i = 0
x=0
n = 30
c=2
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

while c < n:
    fib_sum = fib2 + fib1
    fib1 = fib2
    fib2 = fib_sum
    c= c + 1
    a.append(fib_sum)

a.reverse()

while i < 30:
    if x < a[i]:
        b.append(0)
        i = i + 1
    else:
        b.append(1)
        x = x - a[i]
        i = i + 1

z = 0
while b[z] < 1:
    b.remove(0)
    i = i + 1

b.pop()
print(''.join(map(str, b)))
time.sleep(5)
