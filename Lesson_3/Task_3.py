# Task_3

def my_func(a, b, c):
    if a < b and c:
        return b + c
    elif c > b < a:
        return a + c
    else:
        return a + b



print(my_func(int(input('введите число ')), int(input('введите число ')), int(input('введите число '))))