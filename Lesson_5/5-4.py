f = open('5-4.txt', 'r', encoding= 'utf-8')
text = f.read()
print(text)

with open('res.txt', 'w+', encoding= 'utf-8') as g:
    text = text.replace('One', 'один')
    text = text.replace('Two', 'два')
    text = text.replace('Three', 'три')
    text = text.replace('Four', 'четыре')
    print(text, file=g)
    print(g.read())

f.close()