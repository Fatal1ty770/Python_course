# 1
a = 1
b = '54'
c = a + int(b)
print(c)
print(a + 1 + int(b))
d = int(input('num '))
print (d + c)

# 2
def time(sek):
    hours = sek // 3600
    min = (sek - (hours*3600)) // 60
    sec = sek - (hours * 3600) - (min * 60)
    return (f'чч: {hours} мм: {min} cc: {sec}')

print(time(3700))

# 3
n = (str(input('введите число ')))
s = (int(n) + int(n + n) + int(n + n + n))
print(s)

# 4
i = int(input('введите целое число больше нуля '))
r = -1
while i > 10:
    f = i % 10
    i //= 10
    if f > r:
        r = f
print(r)

# 5
vir = int(input('введите значение выручки '))
izd = int(input('введите значение издержки '))
if vir > izd:
    print('прибыль')
else:
    print('убыток')
prib = vir - izd
print('прибыль', prib)
rent = prib / vir
print('рентабельность ',rent)
sotr = int(input('введите количество сотрудников '))
pns = prib / sotr
print('прибыль на сотрудника ',pns)


# 6
g = (int(input('введите результат в первый день ')))
h = (int(input('введите требуемый результат  ')))
den = 1
while g < h:
    g = g * 1.1
    den = den + 1
print('день на который будет достигнут результат',den)