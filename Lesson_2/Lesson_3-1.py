a = int(input('введите число '))
b = int(input('введите число '))


def delenie(a, b):
    if b == 0:
        return 'error'
    else:
        return a / b


print(delenie(a, b))
