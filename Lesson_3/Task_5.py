# Task_5

def summa ():
    rezult = 0
    exit = False
    while exit == False:
        number = input('Введите числа через пробел или Q для выхода ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                exit = True
                break
            else:
                res = res + int(number[el])
        rezult = rezult + res
        print(f'Текущая сумма равна {rezult}')
    print(f'Итоговая сумма равна {rezult}')


summa()