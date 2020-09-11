f = open('1.txt','w')

n = True
while n == True:
    t = (input('введите текст ', ))
    y = t + '\n'
    f.write(y)

    if t == '':
        n = False

f.close()


g = open('1.txt', 'r')
print(g.read())