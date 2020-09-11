# Task_4

def my_func(x, y):
    return x**y


x= int(input('введите число '))
y= int(input('введите отрицательное число '))

print(my_func(x, y))

# второй вариант


def my_func2(a, b):
    for i in range(abs(b)):
        c = a * a
        rez = 1 / c
    return rez


a= int(input('введите число '))
b= int(input('введите отрицательное число '))

print(my_func2(a, b))