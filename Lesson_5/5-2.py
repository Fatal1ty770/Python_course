f = open('2.txt', 'r')
strok = (f.readlines())
print('количество строк ', len(strok))

f = open('2.txt', 'r', encoding= 'utf-8')
strok = (f.readlines())
s=1
for i in strok:
    i = i.split()
    print(f'количество слов в {s} строке = ', len(i))
    s += 1


f.close()
