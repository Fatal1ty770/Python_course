with open('salary.txt', 'r') as f:
    t = (f.read().split('\n'))
    poor = []
    average = []
    for i in t:
        i = i.split()
        if int(i[1]) < 20000:
            poor.append(i[0])
        average.append(i[1])
    print(f'оклад меньше 20000 у {poor}, средняя зарплата {sum(map(int, average)) / len(average)}')

