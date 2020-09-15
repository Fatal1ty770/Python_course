from itertools import count

for el in count(int(input('Введите начальное число '))):
    print(el)
    if el == 10:
        break

from itertools import cycle

my_list = [True, 'ABC', 123, None]
i = 0
for el in cycle(my_list):
    print(el)
    i += 1
    if i == 10:
        break