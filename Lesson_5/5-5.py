with open('file_5-5.txt', 'w+') as f:
    line = input('Введите цифры через пробел \n')
    f.writelines(line)
    my_numb = line.split()
    print(sum(map(int, my_numb)))