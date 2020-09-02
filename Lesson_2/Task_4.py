# Task 4

a = input()
b = (a.split())
n = 1
for i in b:
    if len(i) > 10:
        i = i[0:10]
    print (n, i)
    n += 1
