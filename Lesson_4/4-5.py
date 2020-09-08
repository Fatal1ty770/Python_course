from functools import reduce


def ymnogenie(x, el):
    return x * el

print(f'Список четных значений {[el for el in range(100, 1001) if el % 2 == 0]}')
print(f'Результат перемножения всех элементов списка {reduce(ymnogenie, [el for el in range(99, 1001) if el % 2 == 0])}')